# https://phidgets.com/?view=api&product_id=DCC1003_0

# https://www.phidgets.com/?tier=3&catid=18&pcid=15&prodid=1118

# https://phidgets.com/?view=code_samples

from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
import time

def onAttach(self):
	print("Attach!")

def onDetach(self):
	print("Detach!")

def main():
	dcMotor0 = DCMotor()

	dcMotor0.setOnAttachHandler(onAttach)
	dcMotor0.setOnDetachHandler(onDetach)

	dcMotor0.openWaitForAttachment(5000)

	dcMotor0.setTargetVelocity(1)

	time.sleep(50)

	dcMotor0.close()

main()
