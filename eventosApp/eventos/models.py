
from django.db import models
from django.forms import ModelForm
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    place = models.CharField(max_length=255)
    address = models.CharField(max_length=400)
    startDate = models.DateField()
    endDate = models.DateField()
    virtual = models.BooleanField()
    created_date = models.DateTimeField('date created', default=timezone.now)


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'category', 'place', 'address', 'startDate', 'endDate', 'virtual']

