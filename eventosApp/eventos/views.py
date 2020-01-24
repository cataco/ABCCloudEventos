import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Event, EventForm


@csrf_exempt
def index(request):
    context = {}
    return render(request, 'eventos/index.html', context)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@csrf_exempt
def events_view(request, event_id=None):
    if request.method == 'GET':
        events_list = Event.objects.order_by('-created_date')
        if event_id is not None:
            events_list = events_list.filter(id=event_id)
        return HttpResponse(serializers.serialize("json", events_list), content_type="application/json")
    elif request.method == 'POST':
        virtual = False
        if request.POST.get('virtual') == 'on':
            virtual = True
        event = Event(
            name=request.POST.get('name'),
            category=request.POST.get('category'),
            place=request.POST.get('place'),
            address=request.POST.get('address'),
            startDate=request.POST.get('startDate'),
            endDate=request.POST.get('endDate'),
            virtual=virtual
        )
        event.save()
        return Response({'message': 'Event was saved'})
    elif request.method == 'PUT':
        event_data = request.data
        Event.objects.filter(id=event_data['id']).update(name=event_data['name'],
                                                         category=event_data['category'], place=event_data['place'],
                                                         address=event_data['address'],
                                                         startDate=event_data['startDate'],
                                                         endDate=event_data['endDate'], virtual=event_data['virtual'])
        event = Event.objects.filter(id=event_data['id'])
        return HttpResponse(serializers.serialize("json", event), content_type="application/json")
    else:
        Event.objects.filter(id=event_id).delete()
        return Response({'message': 'deleted'})


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        password = jsonUser['password']
        email = jsonUser['email']

        user_model = User.objects.create_user(email=email, password=password)
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        email = jsonUser['email']
        password = jsonUser['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            message = "ok"
        else:
            message = 'Email o contraseña incorrectos'

    return JsonResponse({"message": message})


@csrf_exempt
def is_logged_view(request):
    if request.user.is_authenticated():
        message = 'ok'
    else:
        message = 'no'

    return JsonResponse({"message": message})


@csrf_exempt
def add_new_event(request):
    return render(request, "eventos/event_form.html")
