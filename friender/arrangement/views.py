from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import datetime

friends = {
    "Max": [34,"max@mail.ru"],
    "Grigory": [32,"Grigory@mail.ru"],
    "Michael": [29,"Michael@mail.ru"],
    'Pedro': [21,"Pedro@mail.ru"],
    'Kate': [32,"Kate@mail.ru"]
}
establishments = ['Butter bro','Terra','Golden Cafe','Pancakes','Depo']


def main_page(request):
    return render(request,'main.html')

def place_arrangments(request):
    context = {
        "establishments": establishments,
    }
    return render(request, 'establishments.html', context=context)

def all_friends(request):
    context = {
        "friends": friends,
    }
    return render(request,"friends.html",context=context)

