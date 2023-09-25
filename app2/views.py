from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista3(request):
    html= """
       <h1>Vista 1</h1>
       <br>
       <a href="https://www.twitch.tv">twitch</a>
       <br>
       <br>
       <h2>Lorem Ipsum wuajajajajaja</h2>
    """
    return HttpResponse(html)

def vista4(request):
    html= """
       <h1 style="color:red">Vista 2</h1>
       <br>
       <a href="https://www.reddit.com" >Reddit</a>
       <br>
       <br>
       <img src="https://img.freepik.com/vector-gratis/animal-oso-grizzly-sobre-fondo-blanco_1308-65462.jpg?w=360" alt="oso">
    """
    return HttpResponse(html)