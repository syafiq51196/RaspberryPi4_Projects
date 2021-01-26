import time
import RPi.GPIO as GPIO
import math

GPIO_BEGIN_PIN = 4
GPIO_END_PIN = 17

DISTANCE_CM = 52.9 # (in cm) # 52.80cm #52.90 #53.0  
DISTANCE = DISTANCE_CM/100 # (in m)
print("Distance:"+str(DISTANCE)+"m")


TIMEOUT = 5 # (in s)
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
if __name__ == '__main__':
    GPIO.setup(GPIO_BEGIN_PIN, GPIO.IN)
    GPIO.setup(GPIO_END_PIN, GPIO.IN)
    start_time, end_time = 0, 0
    
    while GPIO.input(GPIO_BEGIN_PIN) == GPIO.HIGH:
        time.sleep(0.001)
        start_time = time.time()
    end_time = 0
 
    while GPIO.input(GPIO_END_PIN) == GPIO.HIGH and time.time()-start_time < TIMEOUT:
        time.sleep(0.001)
    else: 
        if time.time()-start_time >= TIMEOUT:
            print ("Timeout")
            exit()
        else:
            end_time = time.time()
            speed = DISTANCE / (end_time - start_time)
            print("Time:"+str(end_time - start_time)+"s")
            print (("Speed:"+"%.4f"+"m/s")%speed)
            