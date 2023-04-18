# https://phidgets.com/?view=api&product_id=DCC1003_0

# https://www.phidgets.com/?tier=3&catid=18&pcid=15&prodid=1118

# https://phidgets.com/?view=code_samples

from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
import time

def onAttach(self):
	print("Attach [" + str(self.getChannel()) + "]!")

def onDetach(self):
	print("Detach [" + str(self.getChannel()) + "]!")

def main():
	dcMotor0 = DCMotor()
	dcMotor1 = DCMotor()

	dcMotor0.setHubPort(5)
	dcMotor0.setChannel(0)
	dcMotor1.setHubPort(5)
	dcMotor1.setChannel(1)

	dcMotor0.setOnAttachHandler(onAttach)
	dcMotor0.setOnDetachHandler(onDetach)
	dcMotor1.setOnAttachHandler(onAttach)
	dcMotor1.setOnDetachHandler(onDetach)

	dcMotor0.openWaitForAttachment(5000)
	dcMotor1.openWaitForAttachment(5000)

	dcMotor0.setTargetVelocity(1)
	dcMotor1.setTargetVelocity(1)

	time.sleep(90)

	dcMotor0.close()
	dcMotor1.close()

main()