
#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.LightSensor import *
#Required for sleep statement
import time
import array 


SD = 2
LightSamples = 200
i = 0
#Create
#accelerometer = Accelerometer()
lightSensor = LightSensor()

#Open
#accelerometer.openWaitForAttachment(1000)
lightSensor.openWaitForAttachment(1000)
print("unput anything to start the loops")
a = input()
print("Light sensor calibration starting", LightSamples, "light samples will be taken" )
while (i < LightSamples):
    SampleSum =+ lightSensor.getIlluminanceNum()
    time.sleep(0.01)
    i =+ 1


#Use your Phidgets
while (True):
    #print("Acceleration: x = " + str(round(accelerometer.getAcceleration()[0],SD)) + " g | y = " + str(round(accelerometer.getAcceleration()[1],SD)) +" g | z = " + str(round(accelerometer.getAcceleration()[2],SD)))
    #time.sleep(.25)
    #I just changed it



#Use your Phidgets
    print("Illuminance: " + float(lightSensor.getIlluminance()) + " lx")
    time.sleep(0.01)
  