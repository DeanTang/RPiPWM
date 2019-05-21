import time

from gpiozero import PWMLED
from gpiozero import DistanceSensor

led = PWMLED(21)

def ping():
    TRIG = 4 
    ECHO = 17
    
    ultrasonic = DistanceSensor(ECHO, TRIG)
    
    distance_m = ultrasonic.distance
    
    return distance_m
    
def controlLED():
    brightness = ping()
    led.value = 1-brightness
    
    time.sleep(1)
    return brightness
    
    
    
    

while True:
    print (controlLED())
