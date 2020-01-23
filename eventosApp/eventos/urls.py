from django.conf.urls import url

from . import views

app_name = 'eventos'

urlpatterns = [
    url(r'^events/$', views.events_view, name='events'),
    url(r'^events/(?P<event_id>\d+)/$', views.events_view, name='event'),

]