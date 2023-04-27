from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
import time

def onAttach(self):
	print("Attach!")

def onDetach(self):
	print("Detach!")

def main():
	dcMotor0 = DCMotor()

	dcMotor0.setHubPort(5)

	dcMotor0.setOnAttachHandler(onAttach)
	dcMotor0.setOnDetachHandler(onDetach)

	dcMotor0.openWaitForAttachment(5000)

	dcMotor0.setTargetVelocity(1)

	time.sleep(90)

	dcMotor0.close()

main()