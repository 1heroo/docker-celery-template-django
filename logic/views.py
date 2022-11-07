from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
import json


def handler(request, exception):
    return redirect('home')


def index(request):
    context = {}
    with open('data.json', 'rb') as data:
        data = data.read()
        data = json.loads(data)
        for i in range(len(data)):
            context.update({f'infos{i + 1}': data[i]})

    return render(request, 'index.html', context=context)
