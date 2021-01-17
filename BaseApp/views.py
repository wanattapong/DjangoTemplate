from django.shortcuts import render, redirect, HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    context = {
        'latest_question_list': 'BaseApp',
    }
    return render(request, 'baseAppHome.html', context)