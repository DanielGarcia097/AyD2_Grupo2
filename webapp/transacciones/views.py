from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def deposito(request):
    template_name = 'transacciones/deposito.html'
    return render(request, template_name)