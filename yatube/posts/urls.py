from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    #  main page
    path('', views.index, name='main'),
    #  group page
    path(
        'group/<slug:slug>/',
        views.group_posts, name='group_list'
    ),
]
