
from django.http import HttpResponse#importante al querer usar django
from django.template import loader
from django.shortcuts import render



import datetime


from django.template import Template

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre

        self.apellido=apellido

def saludo(request): #primera vista

    p1 = Persona("Bruno","Diaz")
    
    temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    
    temasDelCurso1 = []

    '''doc_externo=open("C:/Users/futbo/Documents/Cursos/django/django/ProyectoUno/ProyectoUno/templates/saludo.html")
    plt=Template(doc_externo.read())
    doc_externo.close()'''

    #doc_externo = loader.get_template("saludo.html")
    #ctx = Context()

    #documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "temas":temasDelCurso1})
    
    return render(request, "saludo.html", 
                {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "temas":temasDelCurso}) #las funciones devuelven este tipo de respuiesas para visualizar la pagina

def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = '''
        <html>
        <body>
        <h1>
        Fecha y hora actuales %s
        </h1>
        </body>
        </html
        ''' % fecha_actual
    return HttpResponse(documento)

def calculoEdad(request, edad,agno):
    edadActual=edad
    periodo = agno - 2024
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)

    return HttpResponse(documento)

def ejemplo(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "home.html", {"dameFecha": fecha_actual.date()})