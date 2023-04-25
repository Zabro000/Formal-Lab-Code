
#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
#Required for sleep statement
import time
SD = 2
#Create
accelerometer = Accelerometer()

#Open
accelerometer.openWaitForAttachment(1000)

#Use your Phidgets
while (True):
    print("Acceleration: x = " + str(round(accelerometer.getAcceleration()[0],SD)) + " g | y = " + str(round(accelerometer.getAcceleration()[1],SD)) +" g | z = " + str(round(accelerometer.getAcceleration()[2],SD)))
    time.sleep(.25)
    #I just changed it
  