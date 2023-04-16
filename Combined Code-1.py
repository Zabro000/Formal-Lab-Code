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
MinTimeDifference = 0.15
#accelerometer = Accelerometer()
#accelerometer.openWaitForAttachment(1000)   
#accelerometer = Accelerometer()
lightSensor = LightSensor()
lightSensor.openWaitForAttachment(1000)




#Calculatus the period using time it takes for the light sensor to see the light attached to the arm
def period(BrightnessRegistor,MinTimeDifference):
    CurrentLightValue = lightSensor.getIlluminance()
    Time1 = time.perf_counter() # doesnt change in while loop STAR
    #print("Time1",Time1)
    #print("Time1 =", Time1)
    Time2 = 0
    Period = 0
#need to add if the time is less than resonable then pause the function and say:
    #stop holding the light to the sensor!!
    while(True):
          CurrentLightValue = lightSensor.getIlluminance()
          time.sleep(0.05)
          if(CurrentLightValue > BrightnessRegistor):
              Time2 = time.perf_counter()
              Period = (Time2 - Time1)
              #print("PeriodCheck", Period)
              if(Period < 0.2):
                  #print("Continue")
                  Period = 0
                  continue
              elif(Period > MinTimeDifference):
                  #print("broke")
                  return Period 
                  
          
    
    #Period = time over cycles 
    

def smallperiod():
    Time2 = time.perf_counter()


def cleanprint(Period,MinTimeDifference):
    if(Period < MinTimeDifference):
        return
    print("this is the period,", Period)
    return
   
   
def CSVwrite():
    return
     
## main program starts here ########################################################
SD = int(input("How many decimal places do you want to round to? "))
input("put anything to start the loops. ")
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

i = 0
ProgramCheck = 400
Break = 0
while(Break == 0):
    
    
    LoopTimeStart = time.perf_counter()
    while(True):
        Period = period(BrightnessRegistor,MinTimeDifference)
        LoopTimeStop = time.perf_counter()
        ChangeInLoopTime = LoopTimeStop - LoopTimeStart
        if(ChangeInLoopTime < 0.10):
            continue
        else:
            LoopTimeEnd = time.perf_counter()
            RealPeriod = LoopTimeEnd - LoopTimeStart
            break
    print(" Real Period is ", RealPeriod)
    print(" Period is ", Period)
    #cleanprint(Period,MinTimeDifference)
    
    
    
    
    
    
    
    
    # After some amount of loops this program runs it asks if more observations
    #Still want to be done, using i varbile to count times
    i = i + 1
    
    print(i,"and period", Period)
    if(i >=  ProgramCheck):
        print("Do you want to break out of program? Type, 1 for yes, 2 for no")
        Command = int(input())
        if(Command == 1):
            i = 0
            Break = 1
            print(Break)
            continue
        elif(Command == 2):
            i = 0
            continue
        
print("program ended")
while(True):
    pass
    
        
        

    
    
    
    
    
    
    
