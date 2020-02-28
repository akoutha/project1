import threading
import time
import random
import sys

import socket

def client():


        hostname = sys.argv[1] #hostname
        connectTS = 0 #check to see if TS server is connected or not
        tsHostname = ""
        try:
            cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[C]: Client socket created")
        except socket.error as err:
            print('socket open error: {} \n'.format(err))
            exit()


        if sys.argv[1] == "local":
            localhost_addr = socket.gethostbyname(socket.gethostname())
            print "got local addy"
        else:
            localhost_addr = socket.gethostbyname(hostname)



        server_binding = (localhost_addr, sys.argv[1]) #add rsPort
        cs.connect(server_binding)

        with open("PROJI-HNS.txt") as fp:
            line = fp.readline() #get first line
            line = line.strip() #remove spaces
            file = open("results.txt","w+")
            while line:
                print "This line is: " + line
                cs.sendall(line) #send to rs
                data_from_server=cs.recv(1024) # Receive data from the server
                print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
                dataList = data_from_server.split()  #split data from server

                print dataList

                if dataList[2] == "A": #if available
                    file.write(data_from_server+"\n")
                    print "wrote onto file - RS"
                else: #check TS if not available
                    print "no match in rs table, checking TS table"
                    tsHostname = dataList[0]

                    if dataList[0] == "localhost":
                        tsHostname = socket.gethostname()
                    else:
                        tsHostname = dataList[0]

                    if connectTS == 0: #initial connection to TS
                        print "intial TS connect"
                        connectTS = connectTs(tsHostname)

                    connectTS.sendall(line) #send to ts
                    data_from_server = connectTS.recv(1024) #recv from ts
                    print("[C]: Data received from TS server: {}".format(data_from_server.decode('utf-8')))
                    dataList = data_from_server.split()

                    if dataList[2] == "A":
                        file.write(data_from_server+"\n")
                        print "wrote onto file - TS"
                    else: #not found in any server
                        print "No match in TS - ERROR"
                        file.write(data_from_server+"\n")

                line = fp.readline() #move next line

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
    #localhost_addr = socket.gethostbyname(socket.gethostname())
    localhost_addr = socket.gethostbyname(host)

    # connect to the server on local machine
    server_binding = (localhost_addr, sys.argv[3])
    #print(localhost_addr)
    tcs.connect(server_binding)
    return tcs

if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()
    print("Done.")
