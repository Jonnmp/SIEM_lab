from django.shortcuts import render

def index(request):
    """
    Renderiza el panel principal del SIEM.
    Aquí enviaremos más adelante los datos de las alertas y sensores.
    """
    return render(request, 'dashboard/index.html')