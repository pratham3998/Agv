import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


TRIG=11
ECHO=12


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def distance():
    GPIO.output(TRIG,True)
    
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    print ("Starting measurement")
    
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
        #print("T1")


    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
        #print("T2")

    x = (StopTime-StartTime)
    distance = (x * 34300) / 2
 
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()