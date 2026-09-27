import os
import time

LED_PATH = "/sys/class/leds/ACT/brightness"

def imposta_led(stato):
    with open(LED_PATH, "w") as f:
        f.write(str(stato))

def get_cpu_temp():
    """Legge la temperatura della CPU dal sensore di sistema"""
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = float(f.read()) / 1000.0
    return temp

def get_ram_usage():
    """Legge la memoria RAM usata e totale usando il comando 'free'"""
    stream = os.popen("free -m")
    lines = stream.readlines()
    # Estrae la riga con le informazioni sulla memoria RAM
    ram_info = lines[1].split()
    totale = int(ram_info[1])
    usata = int(ram_info[2])
    percentuale = (usata / totale) * 100
    return usata, totale, percentuale

print("=== MONITOR DI SISTEMA RASPBERRY PI ===")
print("Premi CTRL+C per fermare il monitoraggio.\n")

try:
    while True:
        temp = get_cpu_temp()
        ram_usata, ram_totale, ram_perc = get_ram_usage()

        print(f"🌡️  Temperatura CPU : {temp:.1f}°C")
        print(f"🧠 Memoria RAM     : {ram_usata}MB / {ram_totale}MB ({ram_perc:.1f}%)")

        # Se la CPU supera i 50°C, fa due lampeggi d'avviso
        if temp > 50.0:
            print("⚠️ Temperatura elevata! Avviso LED attivato.")
            for _ in range(2):
                imposta_led(1)
                time.sleep(0.1)
                imposta_led(0)
                time.sleep(0.1)
        else:
            print("STATUS: Ottimo, temperatura nella norma.")

        print("-" * 40)
        time.sleep(3)  # Aggiorna i dati ogni 3 secondi

except KeyboardInterrupt:
    imposta_led(0)
    print("\nMonitoraggio terminato.")