import socket
import threading
import requests
import json
import pickle
import time

DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 9999
SERVER = "0.0.0.0"
ADDR = (SERVER,PORT)

VALID_STATUS_CODE1 = 200
VALID_STATUS_CODE2 = 299

git_url = "https://api.github.com/repos/"

# create a socket
socketServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# bind the socket to the address in ADDR which need s to be in a tuple
socketServer.bind(ADDR)

def talkToAPI(msg):
    repos = msg
    stars = {}

    for repo in repos:
        url = git_url + repo
        r = requests.get(url)
        if VALID_STATUS_CODE1 <= r.status_code <= VALID_STATUS_CODE2:
            repo_data = r.json()
            if repo not in stars:
                stars[repo] = repo_data['watchers']
        else:
            print(f"[ERROR] {repo} not a valid GitHub Repository")
            print(f"[ERROR] get status {r.status_code} received")
    return stars

def handle_client(c, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    try:
        while connected:
            pickedMsg = c.recv(2048)
            msg = pickle.loads(pickedMsg)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                # send the converted list to the get API method
                output = talkToAPI(msg)
            print(f"[{addr}] {msg}")

            # send message to client
            try:
                c.send(pickle.dumps(output))
                time.sleep(1)
                c.send(pickle.dumps("All done"))
            except socket.error as e:
                print(e)

    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        c.close()

def start():
    socketServer.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        c, addr = socketServer.accept() # when it finds a connection, it stores the client under conn and port number under addr
        #handle_client(c,addr)
        thread = threading.Thread(target=handle_client, args=(c,addr))
        thread.start()
        print(F"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
 
# Call the main function here
if __name__ == "__main__":
    print("[STARTING] server is starting ... ")
    start()