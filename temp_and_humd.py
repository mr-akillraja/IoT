import Rpi.GPIO as GPIO
import dht11
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.bcm)

DHT_PIN = 4

instance = dht11.DHT11(pin = DHT_PIN)

try :
    while True:
        result = instance.read()
        if result.is_valid():
            temp = instance.temperature
            humd = instance.humidity
            print(f"Temperature : {temp}")
            print(f"Humidity : {humd}")
except KeyboardInterrupt:
    GPIO.clenup
