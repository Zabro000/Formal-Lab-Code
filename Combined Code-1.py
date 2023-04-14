
#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.LightSensor import *
#Required for sleep statement
import time
import array 
import numpy as np

# remeber to comment lots 


LightSamples = 35
i = 0
SampleSum =  0 
#Create
#accelerometer = Accelerometer()
lightSensor = LightSensor()

#Open
accelerometer.openWaitForAttachment(1000)
lightSensor.openWaitForAttachment(1000)
SD = int(input("How many decimal places do you want to round to?"))
print("put anything to start the loops")
a = input()
print("Light sensor calibration starting", LightSamples, "light samples will be taken" )
while(i < LightSamples):
    i = i + 1
    print(i)
print("done loop")
i = 0
print("Do not change lighting")
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

print("input anything to start the main program")
a = input()
