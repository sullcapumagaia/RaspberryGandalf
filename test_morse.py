import time

LED_PATH = "/sys/class/leds/ACT/brightness"

def imposta_led(stato):
    with open(LED_PATH, "w") as f:
        f.write(str(stato))

def punto():
    """Segnale breve (.) -> 300ms"""
    imposta_led(1)
    time.sleep(0.3)
    imposta_led(0)
    time.sleep(0.3)

def linea():
    """Segnale lungo (-) -> 900ms"""
    imposta_led(1)
    time.sleep(0.9)
    imposta_led(0)
    time.sleep(0.3)

# Funzioni per le singole lettere di GIAN
def lettera_G():
    linea(); linea(); punto()

def lettera_I():
    punto(); punto()

def lettera_A():
    punto(); linea()

def lettera_N():
    linea(); punto()

print("=== TEST CODICE MORSE: GIAN ===")
print("Inizio trasmissione... Premi CTRL+C per fermare.")

try:
    while True:
        print("Trasmetto 'G' (--.)")
        lettera_G()
        time.sleep(1.5)  # Pausa tra le lettere

        print("Trasmetto 'I' (..)")
        lettera_I()
        time.sleep(1.5)

        print("Trasmetto 'A' (.-)")
        lettera_A()
        time.sleep(1.5)

        print("Trasmetto 'N' (-.)")
        lettera_N()

        print("--- 'GIAN' trasmesso! Pausa di 3 secondi prima di ripetere ---\n")
        time.sleep(3)

except KeyboardInterrupt:
    imposta_led(0)
    print("\nTrasmissione interrotta.")