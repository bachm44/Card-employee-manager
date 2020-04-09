import argparse
import sqlite3
import json
import time
import paho.mqtt.client as mqtt

import backend.terminalBack as terminalBack

host_name = "localhost"
client = mqtt.Client()

is_startup = True
terminalID = 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("terminalID", help="TerminalID which will be emulated", type=int)
    args = parser.parse_args()

    global terminalID
    terminalID = args.terminalID

    time_left = 20
    print("Connecting to mosquitto...")
    while time_left != 0:
        try:    
            client.connect(host_name)
            break
        except:
            print("Waiting for mosquitto: ", time_left)
            time_left -= 1

    if time_left == 0:
        print("Cannot connect to mosquitto")
        exit()

    print("Connected") 
    client.on_message=on_message
    id_topic = "terminal/ID/get/" + str(terminalID)
    card_topic = "terminal/card/get/" + str(terminalID)
    client.subscribe(card_topic)
    client.subscribe(id_topic)

    time_left = 20
    client.loop_start()
    while is_startup and time_left != 0:
        print("Waiting for mqttBroker.py...", time_left, "s")
        client.publish("terminal/ID/post", str(terminalID))
        
        time.sleep(1)
        time_left -= 1

    if time_left == 0:
        print("Cannot connect to mqttBroker.py")
        exit()

    client.loop_stop()
    while True:
        client.loop_forever() 


def on_message(client, userdata, message):
    txt_message = str(message.payload.decode("utf-8", "ignore"))
    id_topic = "terminal/ID/get/" + str(terminalID)
    if message.topic == id_topic:
        if txt_message == "False":
            print("In order to use this terminal please first register it!")
            exit()        
        global is_startup
        is_startup = False    
    elif message.topic == ("terminal/card/get/" + str(terminalID)):
        if len(txt_message) > 1:
            print(txt_message)

    cardID = input("Please provide card character or \'exit\' keyword >> ")
    if cardID != 'exit':
        to_send = {"terminalID": terminalID, "cardID": cardID}
        client.publish("terminal/card/post", json.dumps(to_send))
    else:
        client.loop_stop()
        client.disconnect()
        exit()


if __name__ == "__main__":
    main()   