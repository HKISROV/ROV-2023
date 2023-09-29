import time
import wiringpi

#w1-3 (speed forwards)
#s1-3 (speed backwards)


currentDirection = "d"
currentAcc = "0"
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

def keyPress(dir, acc, speed):
    if dir == "w":
        if(150 + acc != speed):
            slowChange(speed, 150 + acc)
        return 150 + acc
    elif dir == "s":
        if (150 - acc != speed):
            slowChange(speed, 150 - acc)
        return 150 - acc
    else: 
        if (150 != speed):
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
    if(len(str(key)) > 1):
        if(1 <= int(key[1]) <=3):
            currentDirection = str(key[0])
            currentAcc = int(key[1]) * 10
            currentSpeed = keyPress(currentDirection, currentAcc, currentSpeed) #Calls function key_press above with value inputed.
        else:
            print("Please attach a speed value that's valid (1-3) inclusive")
    else:
        print("Please enter a number attached to the letter(eg: w1)")
