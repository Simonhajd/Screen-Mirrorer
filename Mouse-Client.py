import time
from pynput.mouse import Listener
import socket
import math

last_sent = time.time()
delay = 1  # delay in seconds

def on_move(x, y):
    global last_sent
    if time.time() - last_sent > delay:
        data = f"{math.floor(x)},{math.floor(y)}"
        print(data)
        client.send(data.encode('utf-8'))
        last_sent = time.time()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12390))

with Listener(on_move=on_move) as listener:
    listener.join()