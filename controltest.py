import time
import wiringpi

pins = [18,12,13]

def keyPress(key):
    if key[0] == "w":
        speed = 180
    elif key[0] == "s":
        speed = 110
    else: 
        speed = 150

    for pin in pins:
        wiringpi.pwmWrite(pin,speed)



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
