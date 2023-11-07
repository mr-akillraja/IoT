import RPi.GPIO as GPIO
import time

PIR_PIN = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.bcm)
GPIO.setup(PIR_PIN,GPIO.IN)

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected")
        time.sleep(2)
except KeyboardInterrupt:
    print("motion stopped by the user")
finally:
    GPIO.cleanup
