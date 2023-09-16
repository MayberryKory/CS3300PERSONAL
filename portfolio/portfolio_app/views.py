from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    #render HTML template index.html with the data in the variable
    return render ( request, 'portfolio_app/index.html')
