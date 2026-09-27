import time

LED_PATH = "/sys/class/leds/ACT/brightness"

def imposta_led(stato):
    """Funzione per accendere (1) o spegnere (0) il LED"""
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

print("=== TEST 2: CODICE MORSE (S.O.S.) ===")
print("Inizio trasmissione... Press CTRL+C per fermare.")

try:
    while True:
        print("Invio 'S' (...)")
        punto(); punto(); punto()
        time.sleep(0.6)

        print("Invio 'O' (---)")
        linea(); linea(); linea()
        time.sleep(0.6)

        print("Invio 'S' (...)")
        punto(); punto(); punto()

        print("--- Sequenza completata. Pausa di 2 secondi ---\n")
        time.sleep(2)

except KeyboardInterrupt:
    imposta_led(0)
    print("\nTrasmissione Morse interrotta.")