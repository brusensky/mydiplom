from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.

def index(requst):
    return HttpResponse("HELLO")
