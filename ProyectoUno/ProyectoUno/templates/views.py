from django.http import HttpResponse#importante al querer usar django

def saludo(request): #primera vista

    return HttpResponse("Hola Pilotos es es mi primera pagina con Django") #las funciones devuelven este tipo de respuiesas para visualizar la pagina