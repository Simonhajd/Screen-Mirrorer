import socket
import pyautogui
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('0.0.0.0', 12390))
serv.listen(5)
pyautogui.PAUSE = 0
while True:
    #print("Waiting for connection")
    conn, addr = serv.accept()
    from_client = b''  # Changed from string to bytes
    
    while True:
        from_client = b''  # Changed from string to bytes
        data = conn.recv(8192)
        if not data:
            break
        from_client += data
        decoded_data = from_client.decode()
        #print(decoded_data)  # Decode bytes to string before printing
        
            
        if decoded_data.startswith('p'):
            #print('pressing:', decoded_data[1:])
            pyautogui.keyDown(decoded_data[1:])  # press the keys after the first character
        elif decoded_data.startswith('r'):
            #print('releasing:', decoded_data[1:])
            pyautogui.keyUp(decoded_data[1:])  # release the keys after the first character

        print('\n')

    conn.close()
    #print('client disconnect')  # Fixed indentation and spelling

    