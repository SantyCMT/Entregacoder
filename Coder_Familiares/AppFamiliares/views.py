from django.shortcuts import render
from AppFamiliares.models import ListadeFamiliares
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def listado_Familiares(request):
    lista_familia = ListadeFamiliares.objects.all()

    cadena = {"listaFamilia": lista_familia,}

    plantilla = loader.get_template("Template.html")

    doc = plantilla.render(cadena)

    return HttpResponse(doc)