import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from django.core import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Event


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication])
def events_view(request, event_id=None):
    if request.method == 'GET':
        events_list = Event.objects.order_by('-created_date')
        if event_id is not None:
            events_list = events_list.filter(id=event_id)
        return HttpResponse(serializers.serialize("json", events_list), content_type="application/json")
    elif request.method == 'POST':
        event_data = request.data
        event = Event.objects.create(**event_data)
        return Response(data=event.id)
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