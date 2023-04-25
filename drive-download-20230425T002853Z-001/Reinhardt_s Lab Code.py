from Phidget22.Phidget import *
from Phidget22.Devices.LightSensor import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.BLDCMotor import *
from Phidget22.Phidget import *
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
LightCoe = -17
MinTimeDifference = 0.05
PeriodTolerance = 0.30

#Varribles for calculations
#in meters and in kilograms, change these
ArmRadius = 0.120 # 22.5 centimeters
ObjectMass = 0.0212 # 0.80 grams

#light sample varribles
LightSamples = 40
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
    
    VelocityC = (2* (3.1415) *ArmRadius)/Period
    AccelC = (VelocityC * VelocityC)/ArmRadius
    ForceT = (ObjectMass * AccelC)
    
    Datalist = [Period, VelocityC, AccelC, ForceT]
    
    with open ('Lab_dataReinhardt.csv','a') as datafile:
        write = csv.writer(datafile)
        write.writerow(Datalist)
    print("Period Data was writen")
          
    return



## main program starts here ##########################################################################################
print("This is the program for Reinhardt's Lab.")
print("Soleniods and motors are being attached...")
dcMotor0 = DCMotor()
dcMotor1 = DCMotor()

dcMotor0.setHubPort(4)
dcMotor0.setChannel(0)
dcMotor1.setHubPort(4)
dcMotor1.setChannel(1)

dcMotor0.openWaitForAttachment(5000)
dcMotor1.openWaitForAttachment(5000)

dcMotor0.setTargetVelocity(1)
dcMotor1.setTargetVelocity(1)







SD = int(input("How many decimal places do you want to round to? "))
MotorSpeed = float(input("Type in a Motor Speed between 1 and 0: "))
print("The motor will start after the light sampling")

time.sleep(4)

input("put anything to start the loops: ")
print("Light sensor calibration starting", LightSamples, "light samples will be taken" )
print("Do not change the lighting of the room")

time.sleep(3)

#finds the average ambient brightness of the room over a number of samples
while (i < LightSamples):
    print(lightSensor.getIlluminance())
    SampleSum = SampleSum + lightSensor.getIlluminance()
    time.sleep(0.3)
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
ProgramCheck = 40
Break = 0
PeriodInital = 0
PeriodFinal = 0

#Motors are now on
bldcMotor0.setTargetVelocity(MotorSpeed)
print("Motors are starting...")

print("Loops starting, motors are on.")

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
    print("loop count ", i)
    print(" ")
    
    #Releases the solenoid if the change in the period is minimal, that is uniform circluar motion. 
    if(-PeriodTolerance < ChangeInPeriod < PeriodTolerance):
        input("Type in anything to release the solenoids: ")
        print(" ")
        while(True):
            #the next time the light sensor is hit it releases the solenoid pins
            CurrentLightValue = lightSensor.getIlluminance()
            time.sleep(0.02)
            if(CurrentLightValue < BrightnessRegistor):
                
                #changed signs for the black paper
                #Relase Solenoids and record Period, VC
                dcMotor0.setTargetVelocity(0)
                dcMotor1.setTargetVelocity(0)
                
                
                CSVwrite(Period,ArmRadius,ObjectMass)
                
                #delay time to keep the motor spinning
                time.sleep(2)
                
                print("Motors will now stop...")
                bldcMotor0.setTargetVelocity(0)
                MotorSpeed = float(input("Type in a mew motor speed between 1 and 0: "))
                bldcMotor0.setTargetVelocity(MotorSpeed)
                
                print("Unplug the solenoids to cool them down wait like a few minutes...")
                print(" ")
                input("Input anything to power the solenoids: ")
                print(" ")
                
                dcMotor0.setTargetVelocity(1)
                dcMotor1.setTargetVelocity(1)
                
                input("Input andything to power the motor and continue the program")
                print(" ")
                bldcMotor0.setTargetVelocity(MotorSpeed)
                break
            
        
    #After some amount of loops this program runs it asks if more observations
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
    
        
        

    
    
    
    
    
    
    
