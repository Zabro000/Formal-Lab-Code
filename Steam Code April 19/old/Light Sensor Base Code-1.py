
#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.LightSensor import *
#Required for sleep statement
import time

#Create
lightSensor = LightSensor()

#Open
lightSensor.openWaitForAttachment(1000)

#Use your Phidgets
while (True):
    print("Illuminance: " + str(lightSensor.getIlluminance()) + " lx")
    time.sleep(0.01)
  