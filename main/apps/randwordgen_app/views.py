# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
# Create your views here.


def index(request):
    if request.session["counter"] < 1:
        request.session['counter'] = 0
    return render(request, 'randwordgen_app/index.html')

def create(request):
    if request.method == 'POST':
        request.session['randomword'] = get_random_string(length=14)
        request.session['counter'] += 1
        return redirect("/")

def reset(request):
    if request.method == 'POST':
        request.session['counter'] = 0
        request.session['randomword'] = ''
    return redirect("/")