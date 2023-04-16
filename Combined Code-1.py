#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.LightSensor import *
#Required for sleep statement
import time
import array 
import numpy as np

# remember to comment lots 


LightSamples = 25
i = 0
SampleSum =  0
LightCoe = 40
MinTimeDifference = 0.001

#accelerometer = Accelerometer()
lightSensor = LightSensor()
#accelerometer.openWaitForAttachment(1000)
lightSensor.openWaitForAttachment(1000)



#Calculatus the period using time it takes for the light sensor to see the light attached to the arm
def period(BrightnessRegistor):
    CurrentLightValue = lightSensor.getIlluminance()
    Time1 = time.perf_counter()
    #print("Time1 =", Time1)
    Time2 = 0
#need to add if the time is less than resonable then pause the function and say:
    #stop holding the light to the sensor!!
    while(CurrentLightValue < BrightnessRegistor):
          CurrentLightValue = lightSensor.getIlluminance()
          time.sleep(0.1)
          if(CurrentLightValue > BrightnessRegistor):
            Time2 = time.perf_counter()
            #print("Time2 =", Time2)
            #print("break")
            break
           
    Period = (Time2 - Time1)
    #Period = time over cycles 
    return Period

<<<<<<< Updated upstream
def cleanprint(Period,MinTimeDifference):
    if(Period < MinTimeDifference):
        return
    print("this is the period,", Period)
    return
    
    
    

=======
<<<<<<< Updated upstream
>>>>>>> Stashed changes

SD = int(input("How many decimal places do you want to round to?"))
print("put anything to start the loops")
a = input()
=======
def cleanprint(Period,MinTimeDifference):
    if(Period < MinTimeDifference):
        return
    print("this is the period,", Period)
    return

#will use later
def CSVwrite():
    return

    
    

## main program starts here ########################################################
SD = int(input("How many decimal places do you want to round to? "))
input("put anything to start the loops. ")
>>>>>>> Stashed changes
print("Light sensor calibration starting", LightSamples, "light samples will be taken" )
print("Loading...")
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


input("Input anything to start the main program. ")

while(True):
    Period = period(BrightnessRegistor)
    cleanprint(Period,MinTimeDifference)
    
    
    
    
