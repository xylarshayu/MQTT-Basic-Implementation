import paho.mqtt.publish as publish

message = input("Enter a message to send: ")
publish.single("iot/topic", payload=message, hostname="test.mosquitto.org")