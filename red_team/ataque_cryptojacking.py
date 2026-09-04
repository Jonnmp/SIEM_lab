import urllib.request
import time

import urllib.request
import time

# Enviamos la bandera 'ataque=cryptojacking' al servidor para activar el malware
OBJETIVO = "http://127.0.0.1:8000/?ataque=cryptojacking"

print("=====================================================")
print("  Iniciando simulación Red Team: Malware Cryptojacking")
print("=====================================================")
print(f"Objetivo: {OBJETIVO}")
print("[+] Inyectando payload minero de Monero (XMR)...")
print(f"[+] Forzando CPU al 100% de carga constante.\n")

try:
    # Mantenemos el ataque activo en un ciclo infinito hasta que presiones Ctrl+C
    while True:
        urllib.request.urlopen(OBJETIVO)
        print("[!] Minando... (Generando estrés térmico en el servidor objetivo)")
        time.sleep(1) # Petición constante cada segundo para mantener el CPU al máximo
except KeyboardInterrupt:
    print("\n[-] Ataque abortado por el operador. Apagando minero...")
except Exception:
    print("[-] Error de conexión. ¿El servidor objetivo colapsó?")