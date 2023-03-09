from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group_posts),
    path(
        'group_page/<int:pk>/',
        views.group_page
    ),
]
