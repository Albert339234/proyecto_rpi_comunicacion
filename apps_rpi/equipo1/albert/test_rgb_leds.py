"""
Nombre: Albert Garcia
Equipo: 1
Dispositivo: LED RGB (WS281B)
Rol: Salida
Descripcion: Cambia el  color del LED EGB segun intervalos de tiempo.
"""

import time
from rpi_ws281x import PixelStrip, Color


#configuracion del LED
LED_COUNT = 1        #numero de LEDs
LED_PIN = 18         #GPIO pin conectado al LED
LED_FREQ_HZ = 800000 #frecuencia de señal en HZ
LED_DMA = 10
LED_BRIGHTNESS = 255 #brillo maximo
LED_INVERT = False
LED_CHANNEL = 0

#Inicializacion del objeto PixelStrip
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()


def loop():
    print("[INFO] Cambindo colores.Ctrl+C para salir.")
    try:
        while True:
            strip.setPixelColor(0, Color(255,0,0))   #Rojo
            strip.show()
            time.sleep(1)

            strip.setPixelColor(0, Color(0,255,0))   #Verde
            strip.show()
            time.sleep(1)

            strip.setPixelColor(0, Color(0,0,255))   #azul
            strip.show()
            time.sleep(1)

    except KeyboardInterrupt:
        strip.setPixelColor(0, Color(0,0,0))  #Apagar
        strip.show()
        print("[INFO] Apagado por el usuario.")

if __name__ == "__main__":
   loop()

