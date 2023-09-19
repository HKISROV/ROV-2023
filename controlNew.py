import time
import wiringpi

pins = [18,12,13]

def slowChange(start, end):
    if end > start:
        for speed in range(start, end, 10):
            for pin in pins:
                wiringpi.pwnWrite(pin, speed)

    if start < end:
        for speed in range (start, end, -10):
            for pin in pins:
                wiringpi.pwmWrite(pin, speed)

def keyPress(key):
    if key[0] == "w":
        if(speed != 180):
            slowChange(speed, 180)
        speed = 180
    elif key[0] == "s":
        if (speed != 110):
            slowChange(speed, 110)
        speed = 110
    else: 
        if (speed != "150"):
            slowChange(speed, 150)
        speed = 150


wiringpi.wiringPiSetupGpio()

for pin in pins:
    wiringpi.pinMode(pin, wiringpi.GPIO.PWM_OUTPUT)
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
    #Sets up all pins

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
#Sets up pwm

for pin in pins:
    wiringpi.pwmWrite(pin,150)
    #Standardises all motors to stop

while True:  #Running code
    key = input("enter: ")
    keyPress(key) #Calls function key_press above with value inputed.
