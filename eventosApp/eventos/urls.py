from django.conf.urls import url

from . import views

app_name = 'eventos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/$', views.events_view, name='events'),
    url(r'^events/(?P<event_id>\d+)/$', views.events_view, name='event'),
    url(r'^addUser', views.add_user_view, name='addUser'),
    url(r'^registerUser', views.register_user_view, name='registerUser'),
    url(r'^login', views.login_view, name='login'),
    url(r'^isLogged/$', views.is_logged_view, name='isLogged'),
    url(r'^addNewEvent', views.add_new_event, name='addNewEvent'),
    url(r'^editEvent/(?P<event_id>\d+)/$', views.edit_event, name='editEvent'),
    # url(r'^viewEvent/(?P<event_id>\d+)/$', views.view_event, name='viewEvent'),
    url(r'^loginUser', views.login_user, name='loginUser'),
    url(r'^logout/$', views.logout_view, name='logout'),



]