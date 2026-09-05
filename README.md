# 🛡️ SIEM Tactic Monitor & SOAR Engine

**Autor:** Jonathan Eric Moo Pech  
**Programa:** Ingeniería en Sistemas Computacionales  
**Institución:** Instituto Tecnológico Superior de Escárcega (ITSE)  
**Área:** Ciberseguridad (Blue Team / SecOps)

---

## 📌 Descripción del Proyecto
Este proyecto es un simulador avanzado de un **Centro de Operaciones de Seguridad (SOC)** con capacidades **SIEM** (Security Information and Event Management) y **SOAR** (Security Orchestration, Automation, and Response). 

A diferencia de los monitores de red tradicionales, este sistema integra ciencias exactas (cálculo diferencial, métodos numéricos, termodinámica y química de materiales) para detectar y mitigar amenazas cibernéticas y físicas en tiempo real, operando bajo un entorno aislado con Docker.

## ⚙️ Stack Tecnológico
* **Backend:** Python 3, Django 5.2
* **Frontend:** HTML5, Tailwind CSS, Chart.js (Monitor Táctico HUD)
* **Infraestructura:** Docker (Contenerización)
* **Testing:** Scripts de simulación APT (Purple Team / Red Team)

---

## 🔬 Modelos Matemáticos y Detección de Amenazas

El núcleo de inteligencia del SIEM se basa en tres vectores de detección:

### 1. Detección de Exfiltración (Cálculo Diferencial)
* **Amenaza:** Robo silencioso de bases de datos.
* **Modelo:** Análisis de gradientes vectoriales. El sistema evalúa la tasa de cambio en la frecuencia de peticiones a rutas sensibles a lo largo del tiempo. Si la pendiente de extracción supera el umbral matemático seguro, se bloquea el origen.

### 2. Detección de DDoS (Métodos Numéricos)
* **Amenaza:** Ataque de Denegación de Servicio Distribuido (Inundación de red).
* **Modelo:** Interpolación lineal sobre ventanas de tiempo móvil (5 segundos). Permite diferenciar entre picos de tráfico orgánico y ráfagas de denegación mediante análisis de volumen sincronizado.

### 3. Detección de Cryptojacking (Física y Química)
* **Amenaza:** Infección por malware de minería (XMR) que genera sobrecalentamiento.
* **Modelo:** 
  * **Termodinámica:** Simulación del calentamiento progresivo del CPU bajo estrés al 100% (Incremento de voltaje a >250W y temperatura hacia el límite térmico).
  * **Ecuación de Arrhenius (Química):** Cálculo de la degradación acelerada y electromigración del silicio cuando la temperatura supera los 70°C, reduciendo la vida útil del hardware exponencialmente.

---

## 🤖 Motor SOAR (Respuesta Autónoma)
El sistema no solo monitorea, sino que actúa. Al detectar que la salud física del servidor cae por debajo del 85% debido a un ataque de Cryptojacking, la Inteligencia Defensiva (SOAR) ejecuta un **Cortafuegos Activo**:
1. Intercepta y bloquea el proceso malicioso.
2. Fuerzan el enfriamiento del hardware.
3. Permite la regeneración del ciclo térmico.
4. Restaura los servicios sin necesidad de un "Kill Switch" total (preservando la Disponibilidad del servidor).

---

## 🚀 Instalación y Ejecución

**1. Levantar el entorno virtualizado:**
\`\`\`bash
docker-compose up --build -d
\`\`\`

**2. Acceder al Monitor Táctico (Blue Team):**
Abrir en el navegador: [http://localhost:8000](http://localhost:8000)

**3. Ejecutar Simulaciones de Ataque (Purple Team):**
Dentro del entorno, ejecutar los scripts de la carpeta `red_team` para auditar las defensas:
* Ataque DDoS: `python ataque_ddos.py`
* Exfiltración: `python ataque_exfiltracion.py`
* Estrés Térmico: `python ataque_cryptojacking.py`
* **Amenaza Persistente Avanzada (APT):** `python ataque_apt.py` (Ejecuta una cadena de ataques coordinados y multihilo para evaluar el SOAR y las gráficas bajo estrés máximo).

---
*Proyecto Integrador desarrollado para la evaluación técnica en arquitectura de sistemas de seguridad.*