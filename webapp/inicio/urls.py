from django.urls import path
from .views import index

urlpatterns = [
    
    #URL Login

    path('inicio/', index.as_view(), name = 'vista'),

]
