from django.shortcuts import render
from django.http import HttpResponse


#def index(reuqest):
#    return HttpResponse
#Commencer avec HttpResponse afin de contrôler que cela fonctionne

def index(request):
    return render(request, 'base.html')

#Quand on utilise les templates, on utilise le render avec les paramètres à appliquer
