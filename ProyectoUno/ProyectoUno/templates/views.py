from django.http import HttpResponse#importante al querer usar django
import datetime

def saludo(request): #primera vista

    return HttpResponse("Hola Pilotos es es mi primera pagina con Django") #las funciones devuelven este tipo de respuiesas para visualizar la pagina

def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = '''
        <html>
        <h1>
        Fecha y hora actuales %s
        </h1>
        </body>
        </html
        ''' % fecha_actual
    return HttpResponse(documento)

def calculoEdad(request, agno):
    edadActual=18
    periodo = 2019 - agno 
    edadFutura = edadActual + periodo

    documento = "<html><body><h2>En el año %s tendras %s años" %(edadFutura, agno)

    return HttpResponse(documento)