from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Seja bem vindo(a) a FLORENCE.AI")
