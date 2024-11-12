from django.http import HttpResponse

def saludo(request): #primera vista

    return HttpResponse("Hola Pilotos es es mi primera pagina con Django")