import paho.mqtt.client as mqtt
import requests

# MQTT broker details
broker = "test.mosquitto.org"
port = 1883
topic = "http/post"

# HTTP endpoint details
url = "https://httpbin.org/post"
headers = {"Content-Type": "application/json"}
payload = {"key": "Hello MQTT from Python! I am George! I am a student at the University of Patras! I am 23 years old!"}

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.publish(topic, str(payload))

def on_publish(client, userdata, mid):
    print("Message published to MQTT topic")
    send_http_request()

# Send HTTP request
def send_http_request():
    response = requests.request("POST", url, headers=headers, data=str(payload))
    print("HTTP response: " + str(response.status_code))
    

# Create MQTT client
client = mqtt.Client()

# Set MQTT callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to MQTT broker
client.connect(broker, port, 60)

# Enable network traffic handling
client.loop_forever()