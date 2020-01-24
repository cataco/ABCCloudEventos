from django.conf.urls import url

from . import views

app_name = 'eventos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/$', views.events_view, name='events'),
    url(r'^events/(?P<event_id>\d+)/$', views.events_view, name='event'),
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^isLogged/$', views.is_logged_view, name='isLogged'),
    url(r'^addNewEvent', views.add_new_event, name='addNewEvent'),
]