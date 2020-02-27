import threading
import time
import random

import socket

def client():

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
    server = '172.31.122.129'
    server_binding = (server, 50788)
    cs.connect(server_binding)
    cs.sendall('www.google.com')
    #cs.sendall(txt);

    # Receive data from the server
    data_from_server=cs.recv(1024)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # close the client socket
    cs.close()
    exit()


if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()
    print("Done.")
