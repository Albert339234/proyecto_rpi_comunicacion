"""
Nombre: Albert Garcia
Equipo: 1
Dispositivo: LED
Rol: Salida
Descripcion: controlar el brillo de un LED usando PWM con raspberry pi.
"""


#Importar las libreias
import time               #para poder hacer pausas(sleep)
import RPi.GPIO as GPIO   #para controlar los pines GPIO del a raspberry pi


#Configuracion del hardware
def setup():
    print("Configurando GPIO para PWM")

    GPIO.setmode(GPIO.BCM)            #numeracion GPIO NO FISICA
    GPIO.setup(18, GPIO.OUT)          #Configuracion del pin 18 como salida

    pwm_led = GPIO.PWM(18, 100)       #Se crea un objeto PWM en el pin 18, frecuencia de 100 HZ
    pwm_led.start(0)                  #inicio del PWM con ciclo de trabajo a 0% (LED apagado)

    return pwm_led


#Funcion principal para cambiar el brillo
def loop (pwm):
    print("Variando el briloo del LED. Ctrl+c para salir.")
    try:
       while True:
           #Aumentar el brillon poco a poco (0% a 100%)
           for duty in range(0,101,5):         #duty: ciclo de trabajo (0-100)
               pwm.ChangeDutyCycle(duty)       #Cambia el brillo de LED
               time.sleep(0.05)               #Configuracion del hardwareespera 50 mlisegundos


 #Disminuir el brillo poco apoco  (100% a 0%)
           for duty in range(100,-1,-5):         #duty: ciclo de trabajo (0-100)
               pwm.ChangeDutyCycle(duty)         #Cambia el brillo de LED
               time.sleep(0.05)                 #Configuracion del hardwareespera 50 mlisegundos

    #	Si el usuario presiona Ctrl+C
    except KeyboardInterrupt:
        pwm.ChangeDutyCycle(0)                      #Apaga el LED
        pwm.stop()                                  #Detenemos el objeto pwm
        GPIO.cleanup()                              #Liberacion de los pines
        print("Codigo interumpido por el usuario")


 #Esta parte se ejecuta solo si se corre este archivo directamente
if __name__ == "__main__":
    pwm_led = setup()               #Llama la funcion setup para preparar el LED
    loop(pwm_led)                   #Empieza el bucle que cambia el brillo del LED


