# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

def index(request):
    if (request.method != 'GET'):
        raise HttpResponseNotAllowed('Method not allowed')  

    return render(request, 'poor_mans_twitter/index.html')