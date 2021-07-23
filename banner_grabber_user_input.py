#a TCP network connection in python using the socket module
#this is a multiport banner­grabbing program to return the service and version of the service running on four ports.
#returns the expected output if the ports are enabled and open.
#and prints a different message if the ports are closed or connection is refused.
#iterates through the list to listen on the ports.

#import the socket module
import socket
#define a list to hold the ports user wants to listen on
Ports = []
#ask the user for the IP address of target
IP = input("Enter the IP address: ")

#defining the length of the Ports list.
while len(Ports) < 4:
    #ask the user for the different ports and stores them in Ports
    Port = input("Enter the port numbers you want to listen on: ")
    Ports.append(Port)
#print the created Ports list from user input
print ('[%s]' % ', '.join(map(str, Ports)))

for i in range (0,4):
    #create a variable and assign it the value of the socket class from the socket module
    s=socket.socket()
    Port = Ports[i]
    print('This is the banner for the port', Port)
    try:
        #use the connect method from the socket module to make a connection to an IP and port
        s.connect((IP, int(Port)))
        #use the receive (recv) method to read bytes of data from the socket and store in the variable answer
        answer = s.recv(2048)
        print(answer)    
        #close the connection
        s.close
    except:
        #output if the connection is refused or port is closed
        print("Unable to connect to the port. No answer")

    
