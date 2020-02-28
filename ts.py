import threading
import time
import random

import socket
import os
import sys


def rs():

    #rsport = sys.argv[]
    table = []
    # print(os.listdir(os.getcwd()))
    populateDNSTable(table)
    # printDNSTable(table)
    # print(findIP("www.google.com", table))

    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    port = sys.argv[1] if len(sys.argv)>1 else 50789
    server_binding = ('', port)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    print('listening on port:', ss.getsockname()[1])
    connection, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))
    while True:
        #connection, addr = ss.accept()
        #try:
        #print ("[S]: Got a connection request from a client at {}".format(addr))
        data = connection.recv(1024).strip()
        if(data == "end"):
            ss.close()
        if data:
            print("Incoming data: " + data)
            result = findIP(data, table)
            print("Outgoing data: " + data)
            connection.sendall(result)

        #finally:
            # Close the server socket
            #ss.close()
    exit()

# If there is a match, sends the entry as a string:
# Hostname IPaddress A
# If there is no match, RS sends the string:
# TSHostname - NS


def findIP(hostname, table):
    found = False
    ns = ""
    for row in table:
        for item in row:
            if item.lower() == "NS".lower():
                ns = row[0]+" " + row[1] + " " + row[2]
            if hostname.lower() == item.lower():
                found = True
                entry = row[0]+" " + row[1] + " " + row[2]
                return entry
    # Not found. return ns record
    if not found:
        return hostname + " - ERROR: HOST NOT FOUND"
    return ns


def populateDNSTable(table):
    with open("PROJI-DNSTS.txt") as f:
        for line in f:
            inner_list = [elt.strip() for elt in line.split(' ')]
            # in alternative, if you need to use the file content as numbers
            # inner_list = [int(elt.strip()) for elt in line.split(',')]
            table.append(inner_list)


def printDNSTable(table):
    for row in table:
        for val in row:
            print '{:4}'.format(val),
        print


if __name__ == "__main__":
    t1 = threading.Thread(name='rs', target=rs)
    t1.start()
