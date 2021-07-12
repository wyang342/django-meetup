from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_groups, name='show_groups'),
    path('new/', views.create_group, name='create_group'),
    path('<int:group_id>/', views.show_group, name='show_group'),
    path('<int:group_id>/edit/', views.edit_group, name='edit_group'),
    path('<int:group_id>/delete/', views.delete_group, name='delete_group'),
]
