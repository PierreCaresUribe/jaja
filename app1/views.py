from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(request):
    html= """
       <h1>Vista 1</h1>
       <br>
       <a href="https://www.google.com" >Google</a>
       <br>
       <br>
       <p>Lorem Ipsum wuajajajajaja</p>
    """
    return HttpResponse(html)

def vista2(request):
    html= """
       <h1 style="color:blue">Vista 2</h1>
       <br>
       <a href="https://www.facebook.com" >Facebook</a>
       <br>
       <br>
       <button>Este boton no hace nada</button>
    """
    return HttpResponse(html)