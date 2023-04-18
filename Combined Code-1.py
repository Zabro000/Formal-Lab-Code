#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.LightSensor import *
from Phidget22.Devices.DCMotor import *
#Required for sleep statement
import time
import array 
import numpy as np

# remember to comment lots 


LightSamples = 25
i = 0
SampleSum =  0
LightCoe = 40
MinTimeDifference = 0.05
lightSensor = LightSensor()
lightSensor.openWaitForAttachment(1000)
PeriodTolerance = 0.10


#in meters and in kilograms, change these
ArmRadius = 40
ObjectMass = 2




#Calculatus the period using time it takes for the light sensor to see the light attached to the arm
def period(BrightnessRegistor,MinTimeDifference,LoopTimeStart):
    Time1 = time.perf_counter() # doesnt change in while loop STAR
    Time2 = 0
    Period = 0
    while(True):
          CurrentLightValue = lightSensor.getIlluminance()
          time.sleep(0.01)
          if(CurrentLightValue > BrightnessRegistor):
              Time2 = time.perf_counter()
              Period = (Time2 - Time1)
              return Period
          
          
def smallperiod():
    Time2 = time.perf_counter()


# def cleanprint(Period,MinTimeDifference):
#     if(Period < MinTimeDifference):
#         return
#     print("this is the period,", Period)
#     return
    
   
def CSVwrite(Period):
    
    with open ('Lab_data.csv','a') as datafile:
        datafile.write(str(Period) + "\n")
        print("Period Data was writen")
        
    
    return


## main program starts here ########################################################
SD = int(input("How many decimal places do you want to round to? "))
input("put anything to start the loops. ")
print("Light sensor calibration starting", LightSamples, "light samples will be taken" )
print("Do not change the lighting of the room")

time.sleep(3)

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
PeriodInital = 0
PeriodFinal = 0

while(Break == 0):
    LoopTimeStart = time.perf_counter()
   
   while(True):
        Period = period(BrightnessRegistor,MinTimeDifference,LoopTimeStart)
        if(Period < MinTimeDifference):
            continue
        else:
            break
    
#    print(" Real Period is ", RealPeriod)
    print("Current period is: ", round(Period,SD))
    #cleanprint(Period,MinTimeDifference)
    PeriodFinal = Period
    print("Inital period is:", round(PeriodInital,SD))
    
    ChangeInPeriod = PeriodFinal - PeriodInital
    
    PeriodInital = PeriodFinal
    print("Final period is: ", round(PeriodFinal,SD))
    print("The change in period is: ", round(ChangeInPeriod,SD))
    
    i = i + 1
    print("loop count ", i)
    print(" ")
    
    if(-PeriodTolerance < ChangeInPeriod < PeriodTolerance):
        input("Type in anything to release the Solenoids ")
        while(True):
            CurrentLightValue = lightSensor.getIlluminance()
            time.sleep(0.02)
            if(CurrentLightValue > BrightnessRegistor):
                #Relase Solenoids and record Period, VC
                CSVwrite(Period)
                break
            
        
    # After some amount of loops this program runs it asks if more observations
    #Still want to be done, using i varbile to count times
    
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
    
        
        

    
    
    
    
    
    
    
