import socket
import threading
import pickle
import re
import time

HEADER = 1024
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = socket.gethostbyname("localhost")
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
client.connect(ADDR)

def sendAndReceiveReposToServer(msg):
    message = pickle.dumps(msg)
    client.send(message)
    time.sleep(1)
    print(pickle.loads(client.recv(2048)))

#TODO : ADD A VALIDATION REGEX STEP HERE
def validateInput(repositoriesInput):
    # check if the org/repo format exists
    for repo in repositoriesInput:
        pass

def main():
    repositoriesInput = []
    # Input number of elemetns
    n = int(input("Enter the number of repositories : "))
    # Enter elements separated by comma
    repositoriesInput = list(map(str,input("Enter the values in org/repo format : ").strip().split(',')))[:n]
    print("The entered list is: \n",repositoriesInput)
    
    # Send the data to server
    sendAndReceiveReposToServer(repositoriesInput)
    sendAndReceiveReposToServer(DISCONNECT_MESSAGE)

# Call the main function here
if __name__ == "__main__":
    main()