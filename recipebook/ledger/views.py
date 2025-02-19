from django.shortcuts import render, HttpResponse

# Create your views here.

def page_one(request):
    return HttpResponse('Test #1.')

def page_two(request):
    return HttpResponse('Test #2.')

def page_three(request):
    return HttpResponse('Test #3.')
