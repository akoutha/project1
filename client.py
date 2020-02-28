import threading
import time
import random
import sys

import socket

def client():

        connectTS = 0
        try:
            cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[C]: Client socket created")
        except socket.error as err:
            print('socket open error: {} \n'.format(err))
            exit()
            #rsHostname = sys.argv[1]

        localhost_addr = socket.gethostbyname(socket.gethostname())
        server_binding = (localhost_addr, 50788) #add rsPort
        cs.connect(server_binding)

        with open("PROJI-HNS.txt") as fp:
            line = fp.readline()
            line = line.strip()
            file = open("test.txt","w+")
            while line:
                print "This line is: " + line
                cs.sendall(line)
                data_from_server=cs.recv(1024) # Receive data from the server
                print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
                dataList = data_from_server.split()  #split data from server

                print dataList

                if dataList[2] == "A":
                    file.write(data_from_server+"\n")
                    print "wrote onto file - RS"
                else: #check TS
                    print "no match in rs table, checking TS table"
                    if connectTS == 0:
                        print "intial TS connect"
                        connectTS = connectTs(50789)

                    connectTS.sendall(line)
                    data_from_server = connectTS.recv(1024)
                    print("[C]: Data received from TS server: {}".format(data_from_server.decode('utf-8')))
                    dataList = data_from_server.split()

                    if dataList[2] == "A":
                        file.write(data_from_server+"\n")
                        print "wrote onto file - TS"
                    else:
                        print "No match in TS - ERROR"
                        file.write(data_from_server+"\n")

                line = fp.readline()

        cs.close()
        connectTS.close()
        exit()




def connectTs(host):
    try:
        tcs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Connect to TS")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
    #tsListenPort = int(sys.argv[3])
    #port = tsListenPort
    localhost_addr = socket.gethostbyname(socket.gethostname())
    #localhost_addr = socket.gethostbyname(host)

    # connect to the server on local machine
    server_binding = (localhost_addr, 50789)
    #print(localhost_addr)
    tcs.connect(server_binding)
    return tcs

if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()
    print("Done.")
