import random
from django.shortcuts import render
from django.http import JsonResponse
from .trie import Trie

motor_siem = Trie()

ips_maliciosas = [
    "192.168.1.100",
    "10.0.0.5",
    "172.16.0.23",
    "203.0.110.42"
]

for ip in ips_maliciosas:
    motor_siem.insertar(ip)

def index(request):
    """
    Renderiza el panel principal del SIEM.
    """
    return render(request, 'dashboard/index.html')

def generar_telemetria(request):
    """ Genera un log de red simulado y lo valida contra el Arbol Trie."""

    if random.random() < 0.20:
        ip_origen = random.choice(ips_maliciosas)
    else:
        ip_origen = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

    puerto = random.choice([80, 443, 22, 21, 3306])

    es_maliciosa = motor_siem.buscar(ip_origen)

    estado = "Bloqueado" if es_maliciosa else "Permitido"

    datos_log = {
        "ip": ip_origen,
        "puerto": puerto,
        "estado": estado,
        "maliciosa": es_maliciosa
    }

    return JsonResponse(datos_log)