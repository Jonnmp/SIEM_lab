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
historial_exfiltracion = []
temperatura_actual = 45.0
voltaje_actual = 120.0
ultimo_ataque_crypto = 0


def index(request):
    """
    Renderiza el panel y escucha los ataques esternos.
    """
    global historial_peticiones, historial_exfiltracion, ultimo_ataque_crypto
    ahora = time.time()

    historial_peticiones.append(ahora)

    if 'descargar_respaldo' in request.GET.get('accion', ''):
        historial_exfiltracion.append(ahora)

    if 'cryptojacking' in request.GET.get('ataque', ''):
        ultimo_ataque_crypto = ahora

    return render(request, 'dashboard/index.html')

def calcular_interpolacion(volumen_anterior, volumen_reciente):
    """
    Calcula la linea base esperada utilizando interpolacion lineal simple.
    """
    tendencia = volumen_reciente - volumen_anterior
    esperado = volumen_reciente + tendencia
    return max(esperado, 5)

def calcular_gradiente(historial, ventana_tiempo, ahora):
    """
    Calcula la tasa de extraccion de datos por segundo
    """

    eventos_ventana = [t for t in historial if ahora - t <= ventana_tiempo]

    if len(eventos_ventana) < 2:
        return 0.0

    dy = len(eventos_ventana)
    dt = eventos_ventana[-1] - eventos_ventana[0]

    if dt == 0:
        return 0.0

    return dy/dt

def generar_telemetria(request):
    global historial_peticiones, historial_exfiltracion, temperatura_actual, voltaje_actual, ultimo_ataque_crypto
    ahora = time.time()

    historial_peticiones = [t for t in historial_peticiones if ahora - t <= 10]
    bloque_anterior = len([t for t in historial_peticiones if 5 < ahora - t <= 10])
    bloque_reciente = len([t for t in historial_peticiones if ahora - t <= 5])
    trafico_esperado = calcular_interpolacion(bloque_anterior, bloque_reciente)
    anomalia_ddos = bloque_reciente > (trafico_esperado * 3)

    historial_exfiltracion = [t for t in historial_exfiltracion if ahora - t <= 30]
    gradiente = calcular_gradiente(historial_exfiltracion, 30, ahora)

    anomalia_exfiltracion = gradiente > 0.2

    # --- Simulacion Fisica y Termodinamica ---
    es_cryptojacking = 'cryptojacking' in request.GET.get('ataque', '')
    es_cryptojacking = (ahora - ultimo_ataque_crypto) <= 2.0

    if es_cryptojacking:
        voltaje_actual = random.uniform(280.0, 310.0) 
        temperatura_actual += (95.0 - temperatura_actual) * 0.15 
    else:
        voltaje_actual = random.uniform(110.0, 130.0)
        temperatura_actual += (45.0 - temperatura_actual) * 0.10

    alerta_cryptojacking = (temperatura_actual > 80.0) and (voltaje_actual > 250.0)

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
        "peticiones_5s": bloque_reciente,
        "anomalia_exfiltracion": anomalia_exfiltracion,
        "gradiente_fuga": round(gradiente, 2),
        "temperatura_c" : round(temperatura_actual, 1),
        "voltaje_w" : round(voltaje_actual, 1),
        "alerta_cryptojacking": alerta_cryptojacking
    }

    return JsonResponse(datos_log)