from os import name
from django.urls import path
from . import views

urlpatterns = [
    # Group urls
    path('', views.show_groups, name='show_groups'),
    path('new/', views.create_group, name='create_group'),
    path('<int:group_id>/', views.show_group, name='show_group'),
    path('<int:group_id>/edit/', views.edit_group, name='edit_group'),
    path('<int:group_id>/delete/', views.delete_group, name='delete_group'),
    path('<int:group_id>/events/', views.show_events, name='show_events'),

    # Event urls
    path('<int:group_id>/events/<int:event_id>/',
         views.show_event, name='show_event'),
    path('<int:group_id>/events/new/', views.create_event, name='create_event'),
]
