from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница,  ---Google--- жди, я иду за тобой!')


def group_posts(request):
    return HttpResponse('Список микро-блогеров и их постов')


def group_page(request, pk):
    return HttpResponse(f'------Блог номер {pk}-----------')
