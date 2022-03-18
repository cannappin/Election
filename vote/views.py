from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("voici l'index de ma page")

