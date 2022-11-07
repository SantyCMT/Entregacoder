from django.shortcuts import render
from AppFamiliares.models import ListadeFamiliares
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def listado_Familiares(request):
    familiares = ListadeFamiliares.objects.all()

    lista_familia = []

    for miembro in familiares:
        lista_familia.append((miembro.name, miembro.age, miembro.date))

    datos = {"listaFamilia": lista_familia,}

    plantilla = loader.get_template("Template.html")

    doc = plantilla.render(datos)

    return HttpResponse(doc)