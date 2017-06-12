#Communication  Model Vastauine Built 1
import json
import paho.mqtt.client as mqtt
import time
from threading import Thread
import threading

#Importing Modules VasDesigned Modules
"""
print("All Modules Imported Sucessfully Waiting 5 Seconds to start")
print(" Press CTRL + C To Terminate NOW ")
time.sleep(2)
print("Welcome to Vastauine - PreAlpha")
"""

import brain
from config import username,password,IP

USERNAME = username()
PASSWORD = password()
IP= IP()

#SUSCRIBER
def call_brain(message):
      print("Call Brain")
      message=message.decode('UTF-8')      	  
      message=(json.loads(message))      	  
      message=brain.brainComm(message)
      if message == True:
            print("Sucessfully Executed")
      else:
            print(message)
      #mqtt_publish("Sucess_BRAIN")
      

def on_connect(client, userdata, flags, rc):
      print("Connected with result code "+str(rc))
      client.subscribe(IP,2)                #Here 2 is QOS Bit

def on_message(client, userdata, msg):
      print("Your message : ", msg.topic+" "+str(msg.payload))     
      message=msg.payload
      t2 = Thread (target=call_brain,args=(message,))
      t2.start()

      
      
def mqtt_client():
      print("MQTT Client")
      client = mqtt.Client()
      client.username_pw_set(USERNAME,PASSWORD)
      client.on_connect = on_connect
      client.on_message = on_message
      client.connect("www.vastauine.com", 1883, 60)      
      client.loop_forever()


t1 = Thread(target=mqtt_client(),args=())
t1.start()


