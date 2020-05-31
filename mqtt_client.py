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

# Callbacks
def on_connect(self, mosq, obj, rc):
      print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
      print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n");

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
t = np.arange(0,20,1) # time vector; create Fs samples between 0 and 10.0 sec.
x = np.arange(0,2,Ts) # signal vector; create Fs samples
y = np.arange(0,2,Ts) # signal vector; create Fs samples
z = np.arange(0,2,Ts) # signal vector; create Fs samples
tilt = np.arange(0,2,Ts) # signal vector; create Fs samples
temp = np.arange(0,2,Ts) # signal vector; create Fs samples
flag = 1
while flag:
    mqttc.loop()
    if temp[0] == 0.001:
        flag = 0
    
total = 20
for i in range(0, total):
    mqttc.loop()
    x[i] = temp[0]
    print(x[i])
    mqttc.loop()
    y[i] = temp[0]
    print(y[i])
    mqttc.loop()
    z[i] = temp[0]
    print(z[i])
    


plt.plot(t,x, label = 'x', color = 'b')
plt.plot(t,y, label = 'y', color = 'r')
plt.plot(t,z, label = 'z', color = 'g')
plt.set_xlabel('Time')
plt.set_ylabel('Acc Vector')
plt.legend()
plt.show()
s.close()
