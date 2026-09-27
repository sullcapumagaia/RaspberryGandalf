import time

LED_PATH = "/sys/class/leds/ACT/brightness"

def imposta_led(stato):
    with open(LED_PATH, "w") as f:
        f.write(str(stato))

print("=== TEST 1: EFFETTO STROBOSCOPICO ===")
print("Avvio lampeggio rapido (50 impulsi)...")

try:
    for i in range(50):
        imposta_led(1)
        time.sleep(0.05)
        imposta_led(0)
        time.sleep(0.05)

    print("Test stroboscopico completato!")

except KeyboardInterrupt:
    imposta_led(0)
    print("\nInterrotto.")