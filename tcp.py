import socket

#IP ='127.0.0.1'
IP ='0.0.0.0'
PORT = 1235
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048

listening_socket = socket.socket()
listening_socket.bind((IP, PORT))

listening_socket.listen(MAXIMUM_QUEUE_SIZE)
print("Hello, I'm waiting for a connection")

while True:

    (client_socket, client_ip_and_port) = listening_socket.accept()
    # (client_ip, client_port) = client_ip_and_port
    
    initial_response ="Hi there what's up?\n".encode()
    client_socket.send(initial_response)
    
    client_message = client_socket.recv(BUFFER_SIZE).decode()
    echo_response = ("You said: " + client_message).encode()
    client_socket.send(echo_response)
    client_socket.close()

# response = "Hi there, here's my response\n".encode()
# client_socket.send(response)

print("See ya later")
#print(client_ip_and_port)