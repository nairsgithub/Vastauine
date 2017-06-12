#BRAIN  Model Vastauine Built 1
#Available App : Button
import sys,os
import json
from button import button



def brainComm(brain):
	data=dict(brain['data'])
	methord=brain['methord']
	app=brain['APP']
	#Add apps Call in elif loop
	if app == 'button':
		BUTTONAPP=button.main(methord,data)
		return(BUTTONAPP)
	else:
		return("Something went wrong. App not found")


	

	
	
