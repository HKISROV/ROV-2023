import time
import wiringpi
from RPIO import PWM

speed = [150, 150]
#speed[0] is left, speed[1] is right

pins = [18,12,13,19]
#Even pins are left, Odd pins are right

def key_press(key): #See last line for fucntion call


    #Old Code (Archive)
    """
    if key == "w":
        speed = 180
    elif key == "s":
        speed = 110
    else: 
        speed = 150

    if int(key) >= 1 and int(key) <= 9:
        speed = int(key)*10 + 1000

    for pin in pins:
        wiringpi.pwmWrite(pin,speed)
    """

    if key[0] == "w": #if the first value is w (front)
        for i in speed:
            i = int(key[1])*10 + 140
            #sets both left and right in the array to the corresponding speed
    
    if key[0] == "s": #if the first value is s (back)
        for i in speed:
            i = 160 - int(key[1])*10
            #sets both left and right in the array to the corresponding speed
    
    if key[0] == "a": #if the first value is a (left)
        speed[0] = int(key[1])*10 + 140 #sets left motor speed to the corresponding value
        speed[1] = 150 #sets right motor speed to stop

    if key[0] == "d": #if the first value is d (right)
        speed[1] = int(key[1])*10 + 140 #sets right motor speed to the corresponding value
        speed[0] = 150 #sets left motor speed to stop

    for pin in pins:
        if(pin % 2 == 0): #If the pin is even
            wiringpi.pwmWrite(pin, speed[0]) #Writes the speed values for left motors

        elif(pin % 2 == 1): #If the pin is odd
            wiringpi.pwmWrite(pin, speed[1])  #Writes the speed values for right motors



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
    key_press(key) #Calls function key_press above with value inputed.


#w1-5 w1 stop w2 slight forward w5 full forward
#s1-5 s1 stop s2 slight backward s5 full backward
#d1-5 s1 stop s2 slight right s5 full right
#a1-5 a1 stop a2 slight left a5 full left
