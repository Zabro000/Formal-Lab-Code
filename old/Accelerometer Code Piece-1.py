#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
#Required for sleep statement
import time
SD = 2

accelerometer = Accelerometer()
accelerometer.openWaitForAttachment(1000)

def accelerationavg():
    Time1 = time.perf_counter()
    Time2 = Time1
    TimePassed = Time2 - Time1
    TimerSet = 4
    while(TimePassed < TimerSet):
        XAccel1 = accelerometer.getAcceleration()[0]
        YAccel1 = accelerometer.getAcceleration()[1]
        ZAccel1 = accelerometer.getAcceleration()[2]
        time.sleep(0.5)
    
    
    
    
    


while (True):
    print("Acceleration: x = " + str(round(accelerometer.getAcceleration()[0],SD)) + " g | y = " + str(round(accelerometer.getAcceleration()[1],SD)) +" g | z = " + str(round(accelerometer.getAcceleration()[2],SD)))
    time.sleep(.25)
    #I just changed it
  