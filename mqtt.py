import paho.mqtt.client as paho
import time
import matplotlib.pyplot as plt
import numpy as np

# https://os.mbed.com/teams/mqtt/wiki/Using-MQTT#python-client

# MQTT broker hosted on local machine
mqttc = paho.Client()

# Settings for connection
# TODO: revise host to your ip
host = "localhost"
topic = "Mbed"
port = 1883

# Callbacks
def on_connect(self, mosq, obj, rc):
      print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
      print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n")

def on_subscribe(mosq, obj, mid, granted_qos):
      print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
      print("Unsubscribed OK")

# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect and subscribe
print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)

Ts = 0.1
t = np.arange(0,20,Ts) # time vector; create Fs samples between 0 and 10.0 sec.
x = np.arange(0,20,Ts) # signal vector; create Fs samples
y = np.arange(0,20,Ts) # signal vector; create Fs samples
z = np.arange(0,20,Ts) # signal vector; create Fs samples
    


fig, ax = plt.subplots(1, 1)
ax.plot(t,x, label = 'x', color = 'b')
ax.plot(t,y, label = 'y', color = 'r')
ax.plot(t,z, label = 'z', color = 'g')
ax.set_xlabel('Time')
ax.set_ylabel('Acc Vector')
ax.legend()
plt.show()

