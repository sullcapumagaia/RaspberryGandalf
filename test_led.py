from gpiozero import LED
from time import sleep

# Sul Raspberry Pi 3 A+ il LED verde integrato si chiama 'led0' (o 'ACT')
led_verde = LED('led0')

print("=== TEST LED VERDE INTEGRATO ===")
print("Premi CTRL + C per fermare lo script.")

try:
    while True:
        led_verde.on()       # Accende il LED verde del Raspberry
        print("LED integrato: ACCESO")
        sleep(3)
        
        led_verde.off()      # Spegne il LED verde del Raspberry
        print("LED integrato: SPENTO")
        sleep(3)

except KeyboardInterrupt:
    print("\nTest completato.")
    # Ripristina il comportamento normale del LED (attività MicroSD)
    led_verde.close()

