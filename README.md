# RaspberryGandalf
## 📝 Registro Attività - [25/09/2026]

### 🔌 Connessione e Gestione Hardware
* **Connessione SSH:** Stabilita connessione remota al Raspberry Pi 3 Model A+ via terminale (`ssh gaia@gandalfilgrigio.local`).
* **Spegningo e Gestione Energia:** Testata la procedura di arresto sicuro via software (`sudo shutdown -h now`) e monitorati i LED di stato (ACT e PWR) prima del disinserimento dell'alimentazione.
* **Controllo Temperatura:** Utilizzato il comando `vcgencmd measure_temp` per verificare la temperatura operativa della CPU.

### 🐙 Sincronizzazione Git & GitHub
* **Configurazione Profilo:** Impostata l'identità globale su Git (`user.name` e `user.email`).
* **Workflow Completo:** Esercitata e consolidata la sequenza di comandi per il tracciamento del codice:
  * `git add` per preparare le modifiche.
  * `git commit` per creare i punti di salvataggio locali.
  * `git push origin main` per inviare i file aggiornati al repository su GitHub.
  * `git pull origin main` per scaricare ed allineare il codice locale con il repository remoto.

### 🐍 Scripting Python & Hardware Testing
* **Primo Script:** Creato ed eseguito il file `test.py` all'interno del repository `RaspberryGandalf`.
* **Controllo LED Integrato:** Realizzato lo script `test_led.py` per prendere il controllo del LED verde di sistema (ACT) del Raspberry Pi tramite l'accesso al file system `/sys/class/leds/ACT/brightness` ed eseguito con privilegi elevati (`sudo python3 test_led.py`).