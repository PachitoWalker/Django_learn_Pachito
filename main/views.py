from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from goods.models import Categories
# функция для обработки запроса. Принимает: request - запрос. Возвращает: response - ответ

# Изначально
# def index(request):
#     return HttpResponse('Home page')

# Конечная
def index(request):

    context = {
            'title': 'HOME - Главная', 
            'content': 'Магазин мебели HOME',
        }

    return render(request, 'main/index.html', context)

# Изначально
# def about(request):
#     return HttpResponse('About page')
def about(request):
    context = {
            'title': 'HOME - О нас', 
            'content': 'О нас',
            'text_on_page': 'Текст о том, какой же я и мой сайт крутой и вообще я в соло создал yandex. ПОНЯЛ?'
        }

    return render(request, 'main/about.html', context)