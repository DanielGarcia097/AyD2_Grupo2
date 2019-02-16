from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def manual(request):
    form = 'hola  mundo'
    template_name = 'inicio/page-login.html'
    return render(request, template_name,{'form': form})

@csrf_exempt
def inicio_sesion(request):
    if request.method == 'POST':
        template_name = 'inicio/vista.html'
        return render(request, template_name,{'form': 'Dentro de if'})
    else:
        template_name = 'inicio/vista.html'
        return render(request, template_name,{'form': 'Fuera de if'})

    return HttpResponse("return this string")

