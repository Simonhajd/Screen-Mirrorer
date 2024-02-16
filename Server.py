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
        
   
        #print("Send character to CLIENT ")
        #input1 = input()  # Changed from raw_input() to input()
        #conn.send(input1.encode())  # Encode string to bytes before sending

        #print("You received from client the next Character")
        from_client = b''  # Changed from string to bytes
        data = conn.recv(4096)
        if not data:
            break
        from_client += data
        print(from_client.decode())  # Decode bytes to string before printing
        pyautogui.write(from_client.decode())
        print('\n')

    conn.close()
    print('client disconnect')  # Fixed indentation and spelling