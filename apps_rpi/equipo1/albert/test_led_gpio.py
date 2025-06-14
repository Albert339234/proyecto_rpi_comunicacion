"""
Nombre: Albert Garcia 
Equipo: 1
Dispositivo: LED
Rol: Salida
Descripcion: Encender un LED conectado al GPIO 17 de la Raspberry pi.
"""

import time
import RPi.GPIO as GPIO

# Setup: configurando com pin de salida
def setup():
    print("configurando GPIO")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
    return 17

# Loop: encender y apagar el LED

def loop(pin):
    print("Encendiendo LED. Ctrl+C para detener.")
    try:
        while True:
            GPIO.output(pin, GPIO.HIGH)
            print("LED encendido")
            time.sleep(1)

            GPIO.output(pin, GPIO.LOW)
            print("LED apagado")
            time.sleep(1)


    except KeyboardInterrupt:
       GPIO.output(pin, GPIO.LOW)
       GPIO.cleanup()
       print("Intento detenido por le ususario.")

if __name__ == "__main__":
    pin_led = setup()
    loop(pin_led)
