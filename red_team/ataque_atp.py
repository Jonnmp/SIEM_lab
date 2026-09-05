import urllib.request
import time
import threading

OBJETIVO = "http://127.0.0.1:8000/"

print("=====================================================")
print("  Iniciando APT: Amenaza Persistente Avanzada        ")
print("=====================================================")
print(f"Objetivo: {OBJETIVO}\n")

# Función para que los hilos ataquen en paralelo
def disparar():
    try:
        urllib.request.urlopen(OBJETIVO)
    except:
        pass

try:
    # FASE 1: Robo de datos sigiloso (Exfiltración)
    print("[+] Fase 1: Robando respaldos (Duración: ~8s)...")
    for _ in range(4):
        urllib.request.urlopen(OBJETIVO + "?accion=descargar_respaldo")
        time.sleep(2)
        
    print("[!] Exfiltración completada.\n")
    time.sleep(2)

    # FASE 2: Infección física (Cryptojacking)
    print("[+] Fase 2: Inyectando minero XMR (Duración: ~45s)...")
    print("[!] Forzando degradación térmica hasta despertar a la IA SOAR...")
    
    # Subimos a 45 ciclos. Esto asegura que la temperatura pase los 90°C 
    # y la salud se desplome por debajo del 85% detonando la defensa.
    for i in range(80):
        try:
            urllib.request.urlopen(OBJETIVO + "?ataque=cryptojacking")
            print(f"    - Hornenado procesador {i+1}/80...")
        except:
            pass # Si el SOAR nos bloquea la conexión a medio camino, ignoramos el error
        time.sleep(1)
        
    print("[!] Fase térmica completada.\n")
    time.sleep(2)

    # FASE 3: Distracción Masiva (DDoS Multi-hilo)
    print("[+] Fase 3: Lanzando tormenta DDoS (Multi-hilo)...")
    
    # 25 ráfagas masivas
    for i in range(25): 
        hilos = []
        # Lanzamos 20 peticiones simultáneas por ráfaga
        for _ in range(20): 
            hilo = threading.Thread(target=disparar)
            hilos.append(hilo)
            hilo.start()
        
        # Esperamos a que los 20 hilos golpeen
        for hilo in hilos:
            hilo.join()
            
        print(f"    - Impacto simultáneo {i+1}/25 completado...")
        time.sleep(0.5) 
            
    print("\n[!] Secuencia APT finalizada. Retirada táctica iniciada.")

except KeyboardInterrupt:
    print("\n[-] Simulación abortada manualmente.")