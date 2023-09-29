import time
import wiringpi

#w1-3 (speed forwards)
#s1-3 (speed backwards)


currentDirection = "d"
currentAcc = "0"
currentSpeed = [150, 150]
#currentSpeed[0] left, currentSpeed[1] is right
1
pins = [18,12]
#18 is left, 12 is right
def slowChange(start, endL, endR):
    speedChange = [[], []]
    # Left Motor 
    if endL > start[0]:
        print("L Called")
        for i in range(start[0]+10, endL+1, 10):
            speedChange[0].append(i)

    if endL < start[0]:
        print("L Called")
        for i in range(start[0]-10, endL-1, -10):
            speedChange[0].append(i)

    # Right Motor
    if endR > start[1]:
        print("R Called")
        for i in range(start[1]+10, endR+1, 10):
            speedChange[1].append(i)

    if endR < start[1]:
        print("R Called")
        for i in range(start[1]-10, endR-1, -10):
            speedChange[1].append(i)

    #Apply speeds

    print(f"L Speeds{speedChange[0]}")
    print(f"R Speeds{speedChange[1]}")

    if len(speedChange[0]) > len(speedChange[1]):
        print("Change Called 1")
        index = 0
        for i in speedChange[0]:
            wiringpi.pwmWrite(pins[0], i)
            print(f"L{i}")
            if index < len(speedChange[1]):
                wiringpi.pwmWrite(pins[1], speedChange[1][index])
                print(f"R{speedChange[1][index]}")
            index += 1
            time.sleep(0.2)
    
    elif len(speedChange[1]) > len(speedChange[0]):
        print("Change Called 2")
        index = 0
        for i in speedChange[1]:
            wiringpi.pwmWrite(pins[1], i)
            print(f"R{i}")
            if index < len(speedChange[0]):
                wiringpi.pwmWrite(pins[0], speedChange[0][index])
                print(f"L{speedChange[0][index]}")
            index +=1
            time.sleep(0.2)

    else:
        print("Change Called 3")
        index = 0
        for i in speedChange[1]:
            wiringpi.pwmWrite(pins[1], i)
            print(f"R{i}")
            wiringpi.pwmWrite(pins[0], speedChange[0][index])
            print(f"L{speedChange[0][index]}")
            index += 1
            time.sleep(0.2)

    del speedChange
            


def keyPress(dir, acc, speed):
    if dir == "w":
        if(150 + acc != speed[0] or 150 + acc != speed[1]):
            print("keypress called")
            slowChange(speed, 150 + acc, 150 + acc)

            for i in range(0,2):
                speed[i] = 150 + acc

        return speed
    
    elif dir == "s":
        if (150 - acc != speed[0] or 150 - acc != speed[1]):
            slowChange(speed, 150 - acc, 150 - acc)

            for i in range(0,2):
                speed[i] = 150 - acc

        return speed
    
    elif dir == "a":
        if (150 != speed[0] or 150 + acc != speed [1]):
            slowChange(speed, 150, 150+acc)

            speed[0] = 150
            speed[1] = 150 + acc 

        return speed

    elif dir == "d":
        if (150 + acc != speed[0] or 150 != speed[1]):
            slowChange(speed, 150+acc, 150)

            speed[0] = 150 + acc
            speed[1] = 150

        return speed      
    
    else: 
        if (150 != speed[0] or 150 != speed[1]):
            slowChange(speed, 150, 150)

            for i in range(0,2):
                speed[i] = 150

        return speed


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
