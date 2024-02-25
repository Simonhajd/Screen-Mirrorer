from pynput.mouse import Controller
import socket
import math
mouse = Controller()
import pyautogui

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12390))
server.listen()

conn, addr = server.accept()

while True:
    data = conn.recv(1024).decode('utf-8')
    if not data:
        break
    print(data + "\n")  
    try:
        x, y = map(int, data.split(','))
        
        pyautogui.moveTo(x, y, 0.1)
    except ValueError:
        print("Received incorrect data format. Expected two values separated by a comma.")