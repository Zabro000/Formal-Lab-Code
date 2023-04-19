#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.LightSensor import *
from Phidget22.Devices.DCMotor import *
#Required for sleep statement
import time
import array 
import numpy as np
import csv

# remember to comment lots 


LightSamples = 25
i = 0
SampleSum =  0
LightCoe = -40
MinTimeDifference = 0.05
lightSensor = LightSensor()
lightSensor.openWaitForAttachment(1000)
PeriodTolerance = 0.10


#in meters and in kilograms, change these
ArmRadius = 0.225
ObjectMass = 0.01

# def motorstart():
#     dcMotor0 = DCMotor()
# 	dcMotor1 = DCMotor()
# 
# 	dcMotor0.setHubPort(5)
# 	dcMotor0.setChannel(0)
# 	dcMotor1.setHubPort(5)
# 	dcMotor1.setChannel(1)
# 
# 	dcMotor0.openWaitForAttachment(5000)
# 	dcMotor1.openWaitForAttachment(5000)
# 
# 	dcMotor0.setTargetVelocity(1)
# 	dcMotor1.setTargetVelocity(1)
# 
# # 	dcMotor0.close()
# # 	dcMotor1.close()

    


#Calculatus the period using time it takes for the light sensor to see the light attached to the arm
def period(BrightnessRegistor,MinTimeDifference,LoopTimeStart):
    Time1 = time.perf_counter() # doesnt change in while loop STAR
    Time2 = 0
    Period = 0
    while(True):
          CurrentLightValue = lightSensor.getIlluminance()
          time.sleep(0.01)
          #when brightness is lowered it jumps back causing same effect
          #print(CurrentLightValue)
          if(CurrentLightValue < BrightnessRegistor):
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
    
def CSVwriteStart():
    print("Opening the data file...")
    with open ('Lab_data.csv','w') as datafile:
          write = csv.writer
             

def CSVwrite(Period,ArmRadius,ObjectMass):
    
    
    VelocityC = (2*(3.1415)*ArmRadius)/Period
    AccelC = (VelocityC * VelocityC)/ArmRadius
    ForceT = ObjectMass*AccelC
    
    Datalist = [Period, VelocityC, AccelC, ForceT]
    
    with open ('Lab_data.csv','a') as datafile:
        write = csv.writer(datafile)
        write.writerow(Datalist)
    print("Period Data was writen")
          
    return



## main program starts here ########################################################
print("Soleniods are being attached...")
dcMotor0 = DCMotor()
dcMotor1 = DCMotor()

dcMotor0.setHubPort(5)
dcMotor0.setChannel(0)
dcMotor1.setHubPort(5)
dcMotor1.setChannel(1)

dcMotor0.openWaitForAttachment(5000)
dcMotor1.openWaitForAttachment(5000)

dcMotor0.setTargetVelocity(1)
dcMotor1.setTargetVelocity(1)


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
        input("Type in anything to release the Solenoids: ")
        while(True):
            CurrentLightValue = lightSensor.getIlluminance()
            time.sleep(0.02)
            if(CurrentLightValue < BrightnessRegistor):
                #changed signs for the black paper
                #Relase Solenoids and record Period, VC
                dcMotor0.setTargetVelocity(0)
                dcMotor1.setTargetVelocity(0)
                CSVwrite(Period, ObjectMass, ArmRadius)
                print("Stop the motor to reset expariment and unplug the solen oids to cool them down.")
                print(" ")
                input("Input anything to continue the program")
                print(" ")
                dcMotor0.setTargetVelocity(1)
                dcMotor1.setTargetVelocity(1)
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
    
        
        

    
    
    
    
    
    
    
