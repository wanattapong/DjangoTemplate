from django.shortcuts import render, redirect, HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    context = {
        'latest_question_list': 'BackEnd',
    }
    return render(request, 'backEndHome.html', context)