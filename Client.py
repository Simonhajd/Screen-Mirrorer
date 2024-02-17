import socket
from pynput.keyboard import Key, Listener
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12390))
start = 0
keys_pressed = {}

time.sleep(3)

def on_press(key):
    key = str(key).replace("'", "").replace("Key.", "")

    if key not in keys_pressed:  # Only send if key was not already pressed
        keys_pressed[key] = True  # Mark key as pressed
        input1 = "p" + key
        client.send(input1.encode('utf-8'))
        print(input1.encode('utf-8'))

def on_release(key):
    key = str(key).replace("'", "").replace("Key.", "")

    if key in keys_pressed:  # Only send if key was already pressed
        del keys_pressed[key]  # Mark key as released
        input1 = "r" + key
        client.send(input1.encode('utf-8'))
        print(input1.encode('utf-8'))

start += 1
if start == 1:
    listener = Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

while True:
    pass

client.close()