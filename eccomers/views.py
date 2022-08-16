from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from  datetime import datetime



def index(request):
    return render(request, 'index_1.html')
