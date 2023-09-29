import time
import wiringpi

currentSpeed = 150
pins = [18,12,13]

def slowChange(start, end):
    if end > start:
        for i in range(start, end+1, 10):
            for pin in pins:
                wiringpi.pwmWrite(pin, i)
                print(i)
            time.sleep(0.2)

    if end < start:
        for i in range(start, end-1, -10):
            for pin in pins:
                wiringpi.pwmWrite(pin, i)
                print(i)
            time.sleep(0.2)

def keyPress(key, speed):
    if key[0] == "w":
        if(speed != 180):
            slowChange(speed, 180)
        return 180
    elif key[0] == "s":
        if (speed != 110):
            slowChange(speed, 110)
        return 110
    else: 
        if (speed != "150"):
            slowChange(speed, 150)
        return 150


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
    currentSpeed = keyPress(key, currentSpeed) #Calls function key_press above with value inputed.
