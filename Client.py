import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12390))
while True:
    
    #from_server = client.recv(4096)
    #print("I received from SERVER %s" %from_server)
    print("Send your character to SERVER")
    input1=input("input:")
    client.send(input1.encode('utf-8'))

client.close()