import threading
import time
import random
import sys

import socket

def client():

    rsHostname = sys.argv[1]
    #rsPort = sys.argv[2]
    #tsPort = sys.argv[3]

    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    #txt = input("prompt...")


    # connect to the server on local machine
    #server = '172.31.122.129'
    server_binding = (localhost_addr, 50788) #add rsPort
    cs.connect(server_binding)
    cs.sendall(rsHostname)
    #cs.sendall(txt);

    # Receive data from the server
    data_from_server=cs.recv(1024)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    info = data_from_server.split()
#    print "status " + info[2]
    if info[2] == "A":
        print "we gucci"
        #print onto resolved.txt
    else:
        #connect to TS server
        cs2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port2 = 00000
        server_binding2 = (localhost_addr, 50788)
        cs2.connect(server_binding2)
        cs.sendall()#send userinput
        data_from_server2 = cs2.recv(1024)
        info2 = data_from_server2.split()
        if info2 == "A":
            print "we gucci"
            #print onto resolved
        else:
            print "not gucci"
            #print error onto resolved




    # close the client socket
    cs.close()
    #cs2.close()
    exit()


if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()
    print("Done.")
