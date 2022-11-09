from django.shortcuts import render
from AppFamiliares.models import ListadeFamiliares
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def listado_Familiares(request):
    familiares = ListadeFamiliares.objects.all()

    datos = {"listaFamilia": familiares}

    plantilla = loader.get_template("template.html")

    doc = plantilla.render(datos)

    return HttpResponse(doc)