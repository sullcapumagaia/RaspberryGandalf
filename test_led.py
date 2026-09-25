import time

# Percorso di sistema del LED verde (ACT) su Raspberry Pi
LED_PATH = "/sys/class/leds/ACT/brightness"

print("=== TEST LED VERDE INTEGRATO ===")
print("Premi CTRL + C per fermare lo script.")

try:
    while True:
        # Accende il LED
        with open(LED_PATH, "w") as f:
            f.write("1")
        print("LED integrato: ACCESO")
        time.sleep(3)

        # Spegne il LED
        with open(LED_PATH, "w") as f:
            f.write("0")
        print("LED integrato: SPENTO")
        time.sleep(3)

except KeyboardInterrupt:
    print("\nTest completato.")
    # Spegne il LED all'uscita
    with open(LED_PATH, "w") as f:
        f.write("0")

