
#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.LightSensor import *
#Required for sleep statement
import time
import array 
import numpy as np

# remeber to comment lots 


LightSamples = 25
i = 0
SampleSum =  0
LightCoe = 40

#Create
#accelerometer = Accelerometer()
lightSensor = LightSensor()

#Open
#accelerometer.openWaitForAttachment(1000)
lightSensor.openWaitForAttachment(1000)

#Calculatus the period using time it takes for the light sensor to see the light attached to the arm
def period(BrightnessRegistor):
    CurrentLightValue = lightSensor.getIlluminance()
    Time1 = time.perf_counter()
    print("Time1 =", Time1)
    Time2 = 0
#need to add if the time is less than resonable then pause the function and say:
    #stop holding the light to the sensor!!
    while(CurrentLightValue < BrightnessRegistor):
          CurrentLightValue = lightSensor.getIlluminance()
          time.sleep(0.2)
          if(CurrentLightValue > BrightnessRegistor):
            Time2 = time.perf_counter()
            print("Time2 =", Time2)
            print("break")
            break
        
        
    Period = (Time2 - Time1)
    #if statement prevents terminal output if the light is just held up to photosensor
    if(Period < 0.001):
        return
    
    print("period = ", Period)
    
    #Period = time over cycles 
    return Period


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
        #when the amount of times ran is over the brightness to registor a period is callculated
        #the average brightness is also calculated
        #loop is broken
        AverageBrightness = SampleSum/LightSamples
        BrightnessRegistor = AverageBrightness + LightCoe
        print("Average brightness is,", round(AverageBrightness,SD))
        print("done :)")
        break


print("out of the loop now ahh")

print("input anything to start the main program")
a = input()
while(True):
   Period = period(BrightnessRegistor)
   print("this is the period,", Period)
    
    
