from random import sample

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def show_index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    select_fruit = sample(fruits,3)
    content = '<h1>今天吃什么</h1>'
    content += '<hr>'
    content += '<ul>'
    for fruit in select_fruit:
        content += f'<li>{fruit}<li>'
    content += '<ul>'
    return HttpResponse(content)
