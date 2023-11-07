import RPi.GPIO as GPIO
import time


sound_pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.bcm)
GPIO.setup(sound_pin,GPIO.IN)

try:
    while True:
        if GPIO.input(sound_pin):
            print("sound detected")
        time.sleep(2)
except KeyboardInterrupt:
    print("sound not detected")
finally:
    GPIO.cleanup()
