
#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.LightSensor import *
#Required for sleep statement
import time
import array 
import numpy as np

# remeber to comment lots 

SD = 2
LightSamples = 70
i = 0
SampleSum =  0 
#Create
#accelerometer = Accelerometer()
lightSensor = LightSensor()

#Open
#accelerometer.openWaitForAttachment(1000)
lightSensor.openWaitForAttachment(1000)
print("unput anything to start the loops")
a = input()
print("Light sensor calibration starting", LightSamples, "light samples will be taken" )
while(i < LightSamples):
    i = i + 1
    print(i)
print("done loop")
i = 0
while (i < LightSamples):
    #SampleSum =+ lightSensor.getIlluminance()
    print(lightSensor.getIlluminance())
    SampleSum = SampleSum + lightSensor.getIlluminance()
    time.sleep(0.2)
    i = i + 1
    print("Cycles =", i)
    if i == LightSamples:
        AverageBrightness = SampleSum/LightSamples
        print("Average brightness is,", round(AverageBrightness,SD))
        print("done :)")
        break

print("out of the loop now ahh")

#Use your Phidgets
#while (True):
    #print("Acceleration: x = " + str(round(accelerometer.getAcceleration()[0],SD)) + " g | y = " + str(round(accelerometer.getAcceleration()[1],SD)) +" g | z = " + str(round(accelerometer.getAcceleration()[2],SD)))
    #time.sleep(.25)
    #I just changed it



    #Use your Phidgets
    #print("Illuminance: " + float(lightSensor.getIlluminance()) + " lx")
    #time.sleep(0.01)
