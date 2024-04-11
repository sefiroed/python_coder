from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    return HttpResponse("¡Hola Django!")


def segunda_vista(request):
    return HttpResponse("<h1>Segunda vista</h1>")


def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")


def template(request):
    mi_html = open("./template/template1.html")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context({"saludo": "Bienvenido",
                           "autor": "Coderhouse"})
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)
