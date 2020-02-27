import threading
import time
import random
import sys

import socket
def client():

    print 'Args list: ' + str(sys.argv)

    rsHostname = sys.argv[1]
    rsPort = sys.argv[2]
    tsPort = sys.argv[3]

    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #    cs2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = 50007
    #port2 = 50008
    #localhost_addr = socket.gethostbyname(socket.gethostname())
    rsServer_addr = socket.gethostbyname(socket.gethostname())

    #txt = input("prompt...")


    # connect to the server on local machine
    server_binding = (rsHostname, rsPort)
    #server_binding2 = (localhost_addr, port2)


    cs.connect(server_binding)
    #cs2.connect(server_binding2)
    cs.sendall('www.google.com') #send hostname to server
    #cs.sendall('hello world!!')
    #cs2.sendall('goodbye world!!')
    #cs.sendall(txt);

    # Receive data from the server
    data_from_server=cs.recv(1024)

    if(data_from_server == 'A')
        #print onto resolved.txt
    else #else not A, go check TS server
        try:
            cs2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            exit()


        port2 = 5008
        server_binding2 = (localhost_addr, port2)
        cs2.connect(server_binding2)
        cs.sendall('text') #send hostname to server
        data_from_server2 = cs2.recv(1024) #get

        if(data_from_server == 'A') #if found on TS server
            #print onto resolved.txt
        else
            #print hostname error on resolved.txt



    #data_from_server2 = cs2.recv(1024)
#    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
    #print("[C]: Data received from server2: {}".format(data_from_server2.decode('utf-8')))

    # close the client socket
    cs.close()
    cs2.close()
    exit()
