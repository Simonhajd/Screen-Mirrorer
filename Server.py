import socket
import pyautogui
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('localhost', 12390))
serv.listen(5)

while True:
    print("Waiting for connection")
    conn, addr = serv.accept()
    from_client = b''  # Changed from string to bytes
    
    while True:
        from_client = b''  # Changed from string to bytes
        data = conn.recv(4096)
        if not data:
            break
        from_client += data
        decoded_data = from_client.decode()
        print(decoded_data)  # Decode bytes to string before printing
        
            

        if decoded_data.startswith('p'):
            print('pressing:', decoded_data[1:])
            pyautogui.keyDown(decoded_data[1:])  # press the keys after the first character
        elif decoded_data.startswith('r'):
            print('pressing:', decoded_data[1:])
            pyautogui.keyUp(decoded_data[1:])  # release the keys after the first character

        print('\n')

    conn.close()
    print('client disconnect')  # Fixed indentation and spelling