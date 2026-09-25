import sys
import time

print("=== TEST RASPBERRY PI ===")
print(f"Versione Python in uso: {sys.version}")

# Simula un conteggio o un ciclo di test
for i in range(1, 6):
    print(f"Test in corso... Passaggio {i}/5")
    time.sleep(1)

print("=== TEST COMPLETATO CON SUCCESSO! ===")
