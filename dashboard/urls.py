from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/telemetria/', views.generar_telemetria, name='telemetria'),
]