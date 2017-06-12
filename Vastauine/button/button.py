
#GPIO  Model Vastauine Built 1
import time

def GpioUpdate(pin,state):  
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,state)
    time.sleep(0.01)
	return True
	


def main(methord,data):
	if (methord == 'GpioUpdate'):
		for pin in data:			
			Rpin=int(pin[4:]);Rdata=int(data[pin]);
			try:
				res=GpioUpdate(Rpin,Rdata)
			except Exception as e:
				print("Methord sent by server is not Recognised.This may occur when a new update is available.or some misconfiguration")
				print(e)
			else:
				if res == True:
                        		print ('Sucessfully updated :'+ pin )

                        	else :
                               	 	print ('Error Processing'+pin)
                return True
	else:
		print("Methord sent by server is not Recognised.This may occur when a new update is available.")
	return "Button app closed without completion :"

