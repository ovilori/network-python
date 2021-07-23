#TCP listener to listen to information from outsiders to a host.
#the program creates a socket on any port of a host such that when someone connects to that socket, 
#it collects key information about the connector’s system
import socket
#TCP/IP address of the host
TCP_IP = input("Enter the IP address: ")
#port to listen on
TCP_PORT = input("Enter the port number: ")
#buffer size of data to capture
BUFFER_SIZE = input("Enter the buffer size: ")

#defining the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to the IP address and port
s.bind((TCP_IP,int(TCP_PORT)))
#tell the socket to listen using the listen() method from the socket library
s.listen(1)
#capture the IP address and port of the connecting system using the accept () method
conn,addr=s.accept()
#display the IP address and port of the connecting system captured above
print("Connection address: ", addr)
while 1:
    #place the information from the connecting system into a buffer
    data=conn.recv(int(BUFFER_SIZE))
    if not data:
        break
    #print the information
    print("Recieved data: ", data)
    conn.send(data) #echo
    #close the connection
    conn.close
