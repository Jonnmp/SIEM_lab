import random
import time
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

historial_peticiones = []


def index(request):
    """
    Renderiza el panel visual y registra cada impacto del atauqe DDoS
    """
    global historial_peticiones
    historial_peticiones.append(time.time())
    return render(request, 'dashboard/index.html')

def calcular_interpolacion(volumen_anterior, volumen_reciente):
    """
    Calcula la linea base esperada utilizando interpolacion lineal simple.
    """
    tendencia = volumen_reciente - volumen_anterior
    esperado = volumen_reciente + tendencia
    return max(esperado, 5)

def generar_telemetria(request):
    global historial_peticiones
    ahora = time.time()

    historial_peticiones = [t for t in historial_peticiones if ahora - t <= 10]
    bloque_anterior = len([t for t in historial_peticiones if 5 < ahora - t <= 10])
    bloque_reciente = len([t for t in historial_peticiones if ahora - t <= 5])

    trafico_esperado = calcular_interpolacion(bloque_anterior, bloque_reciente)
    anomalia_ddos = bloque_reciente > (trafico_esperado * 3)

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
        "maliciosa": es_maliciosa,
        "anomalia_ddos": anomalia_ddos,
        "peticiones_5s": bloque_reciente
    }

    return JsonResponse(datos_log)