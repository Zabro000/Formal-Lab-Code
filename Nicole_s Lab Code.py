from Phidget22.Phidget import *
from Phidget22.Devices.LightSensor import *
from Phidget22.Devices.BLDCMotor import *
import time
import array 
import numpy as np
import csv

lightSensor = LightSensor()
lightSensor.openWaitForAttachment(1000)
bldcMotor0 = BLDCMotor()

bldcMotor0.setHubPort(3)

bldcMotor0.openWaitForAttachment(5000)



#Varribles for code
LightCoe = -40
MinTimeDifference = 0.05
PeriodTolerance = 0.10
MotorSpeed = 0
#Varribles for calculations
#in meters and in kilograms, change these
ArmRadius = 0.225
ObjectMass = 0.0008

#light sample varribles
LightSamples = 30
i = 0
SampleSum =  0

#Calculatus the period using time it takes for the light sensor to see the light attached to the arm
def period(BrightnessRegistor,MinTimeDifference,LoopTimeStart):
    Time1 = time.perf_counter() 
    Time2 = 0
    Period = 0
    while(True):
          CurrentLightValue = lightSensor.getIlluminance()
          time.sleep(0.01)
          
          #Measures when brightness goes down as a result of the black paper
          if(CurrentLightValue < BrightnessRegistor):
              Time2 = time.perf_counter()
              Period = (Time2 - Time1)
              return Period
          
#opens or creates the csv file       
def CSVwriteStart():
    print("Opening the data file...")
    with open ('Lab_data.csv','w') as datafile:
          write = csv.writer
          
          
          
#writes all data to a csv file for later use in graphing
def CSVwrite(Period,ArmRadius,ObjectMass):
    
    VelocityC = (2 * 3.1415 * ArmRadius)/Period
    AccelC = (VelocityC * VelocityC)/ArmRadius
    ForceT = (ObjectMass * AccelC)
    
    Datalist = [Period, VelocityC, AccelC, ForceT]
    
    with open ('Lab_dataNicole.csv','a') as datafile:
        write = csv.writer(datafile)
        write.writerow(Datalist)
    print("Period Data was writen")
          
    return



## main program starts here ##########################################################################################
print("This is the program for Nicole's Lab.")

SD = int(input("How many decimal places do you want to round to? "))
MotorSpeed = float(input("Type in a Motor Speed between 1 and 0: "))
print("Motor will start after the light sampling")

time.sleep(4)

input("put anything to start the loops: ")
print("Light sensor calibration starting", LightSamples, "light samples will be taken" )
print("Do not change the lighting of the room")

time.sleep(3)


#finds the average ambient brightness of the room over a number of samples
while (i < LightSamples):
    print(lightSensor.getIlluminance())
    SampleSum = SampleSum + lightSensor.getIlluminance()
    time.sleep(0.4)
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


input("Input anything to start the main program, MOTORS WILL START: ")

#Varribles for main loop are created
i = 0
Break = 0
PeriodInital = 0
PeriodFinal = 0
Cycles = 20

bldcMotor0.setTargetVelocity(MotorSpeed)

while(Break == 0):
    LoopTimeStart = time.perf_counter()
   
   #finds the period between each change in brightness
   #if and else statment top changes from reistering if the brightness is constantly different
    while(True):
        Period = period(BrightnessRegistor,MinTimeDifference,LoopTimeStart)
        if(Period < MinTimeDifference):
            continue
        else:
            break
    
    print(" ")
    print("Current period is: ", round(Period,SD))
    PeriodFinal = Period
    print("Inital period is:", round(PeriodInital,SD))
    
    ChangeInPeriod = PeriodFinal - PeriodInital
    
    PeriodInital = PeriodFinal
    
    print("Final period is: ", round(PeriodFinal,SD))
    print("The change in period is: ", round(ChangeInPeriod,SD))
    
    i = i + 1
    print("Cycles: ", i)
    print(" ")
    
    # uses an if statement with two conditions
    # iterations of the loop has to be alot to give the time for the motor ot warm up
    # the period has to be the same (uniform circluar motion )
    # data is then collected
    if(i >= Cycles) and (-PeriodTolerance < ChangeInPeriod < PeriodTolerance):
        input("Type in anything to release measure the system: ")
        print(" ")
        
        CSVwrite(Period,ArmRadius,ObjectMass)
        print("Motors will Now Stop")
        bldcMotor0.setTargetVelocity(0)
        
        MotorSpeed = float(input("Type in a mew motor speed between 1 and 0: "))
        
        bldcMotor0.setTargetVelocity(MotorSpeed)
        
        input("Input anything to continue the program: ")
        print(" ")
        i = 0
            
    
    
    
        
        

    
    
    
    
    
    
    
