from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return HttpResponse('<h1>My first page</h1>')


def post_list(request):
    return HttpResponse('<h1>post list</h1>')


def post_create(request):
    return HttpResponse('<h1>post create</h1>')


def post_delete(request):
    return HttpResponse('<h1>post delete</h1>')
