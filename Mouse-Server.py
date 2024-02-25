import socket
import pyautogui
from pynput.mouse import Controller
import math

mouse = Controller()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12390))
server.listen()

conn, addr = server.accept()

while True:
    # Clear the socket's receive buffer before reading data
    conn.setblocking(0)
    try:
        while True:
            conn.recv(1024)
    except BlockingIOError:
        pass
    conn.setblocking(1)

    data = conn.recv(1024).decode('utf-8')
    if not data:
        break
    for point in data.strip().split('\n'):
        print(point + "\n")  
        try:
            x, y = map(int, point.split(','))
            pyautogui.moveTo(x, y, 0)
        except ValueError:
            print("Received incorrect data format. Expected two values separated by a comma.")