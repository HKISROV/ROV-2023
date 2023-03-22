import time
import wiringpi

speed = 150
pins = [18,12]

def key_press(key):
    if key == "w":
        speed = 180
    elif key == "s":
        speed = 110
    else: 
        speed = 150
    for pin in pins:
        wiringpi.pwmWrite(pin,180)

wiringpi.wiringPiSetupGpio()

for pin in pins:
    wiringpi.pinMode(pin, wiringpi.GPIO_PWM_OUTPUT)
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

for pin in pins:
    wiringpi.pwmWrite(pin,150)

while True:
    key = input("enter: ")
    key_press(key)
