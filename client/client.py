import socket
import threading
import pickle
import re
import time

HEADER = 2048
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 9999
SERVER = "0.0.0.0"
ADDR = (SERVER,PORT)

def createSocket():
    # create a socket
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    return server

def connectToServer(ADDR, server):
    # bind the socket to the address in ADDR which need  s to be in a tuple
    server.connect(ADDR)

def sendAndReceiveReposToServer(msg, server):
    message = pickle.dumps(msg)
    server.send(message)
    time.sleep(1)
    print(pickle.loads(server.recv(2048)))

#TODO : ADD A VALIDATION REGEX STEP HERE
def validateInput(repositoriesInput):
    # check if the org/repo format exists
    pass

def main():
    # create the socket
    server = createSocket()
    # bind it to port
    connectToServer(ADDR, server)

    repositoriesInput = []
    # Input number of elemetns
    n = int(input("Enter the number of repositories : "))
    # Enter elements separated by comma
    repositoriesInput = list(map(str,input("Enter the values in org/repo format : ").strip().split(',')))[:n]
    print("The entered list is: \n",repositoriesInput)
    
    # Send the data to server
    sendAndReceiveReposToServer(repositoriesInput, server)
    sendAndReceiveReposToServer(DISCONNECT_MESSAGE, server)

# Call the main function here
if __name__ == "__main__":
    main()