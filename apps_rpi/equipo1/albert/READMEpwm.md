#control de LED con PWM en Raspberry pi

**Nombre:** Albert Garcia
**Equipo:** 1
**Dispositivo:** LED
**Rol:** salida
**ubicacio del codigo:** `apps_rpi/equipo1/albert/test_led_pwm.py`

------------------------------------------------------------------------------

##Investigacion
El PWM(Pusle width Modulation) permite controlar dispositivos analogos usando una señal digital. 
En Raspberry pi, el modulo `RPi.GPIO`ofrece control por sofware para simular PWM sobre cualquier pin GPIO, aunque el **GPIO 18** es el mas eficiente por soportar PWM por hardware.
El PWM varia en el tiempo que la señal esta en alto (duty cicle), lo que se interpreta como variaciones de potencia. en el caso del led, se traduce a mas o menos brillo.

##Explicacion del codigo 
-`import RPi.GPIOas GPIO`Y` import time`: permiten controlar pines y pausas.
-`setup()`: configura el GPIO 18 com salida y crea el objeto `PWM `con 100HZ.
-`loop(pwm)`: modifica el brillo aumenta y luego disminuye el ciclo de trabajo de duty cicle.
-`try y except`: permite detener el script con Ctrl+C y apaga el LED.

##Aprendizaje
-Implementacion de bloques `try/except`para manejar interupcinoes de forma segura.
-Uso del comando `sudo`para ejecutar script con permisos elevados. esto es necesario para accerde al hardware como los pines GPIO, ya que un usuario normal no tiene permiso para manipularlos directos.


