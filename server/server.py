import socket
import threading
import requests
import json
import pickle
import time

from service import talkToAPI

DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 9999
SERVER = "0.0.0.0"
ADDR = (SERVER,PORT)

VALID_STATUS_CODE1 = 200
VALID_STATUS_CODE2 = 299
GIT_REPO_URL = "https://api.github.com/repos/"

def createSocket():
    # create a socket
    socketServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    return socketServer

def bindSocket(ADDR, socketServer):
    # bind the socket to the address in ADDR which need  s to be in a tuple
    socketServer.bind(ADDR)

def readFromClient(c, addr):
    pickledMsg = c.recv(2048)
    msg = pickle.loads(pickledMsg)
    return msg

def sendResponseToClient(c,stars,error_code):
    try:
        print("*****stars before sending to client***")
        print(stars)
        c.send(pickle.dumps(error_code))
        c.send(pickle.dumps(stars))
        
    except socket.error as e:
        print(e)

def handle_client(c, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    try:
        while connected:
            msg = readFromClient(c, addr)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                # send the converted list to the get API method
                stars,error_code = talkToAPI(msg)
                print(stars,"received the stars in server from api")
            print(f"[{addr}] {stars}")

            # send message to client
            sendResponseToClient(c, stars, error_code)

    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        c.close()

def startServer():
    # create the socket
    socketServer = createSocket()
    # bind it to port
    bindSocket(ADDR,socketServer)
    # listen for a client to access the server
    socketServer.listen()

    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        c, addr = socketServer.accept() # when it finds a connection, it stores the client under c and port number under addr
        thread = threading.Thread(target=handle_client, args=(c,addr))
        thread.start()
        print(F"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
 
# Call the startServer function here
if __name__ == "__main__":
    print("[STARTING] server is starting ... ")
    startServer()