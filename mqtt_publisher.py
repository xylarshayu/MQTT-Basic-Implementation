import paho.mqtt.publish as publish

username = input("Enter a username: ")

try:
    while True:
        message = input("Enter a message to send: ")
        publish.single(f"iot/topic/{username}", payload=message, hostname="test.mosquitto.org")
except KeyboardInterrupt:
    print(f"\nGoodbye {username} !")