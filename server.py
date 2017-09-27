import sys
from datetime import datetime
from time import sleep
import socket
import cv2

server_address = (sys.argv[1], 5000)
max_size = 4096


def main():
    print('Starting the server at', datetime.now())
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(server_address)
    server.listen(5)
    client, addr = server.accept()

    while True:
        cv_p = client.recv(max_size)
        hcrs = client.recv(max_size)

        cv_p = list(map(eval, cv_p.split()))
        hcrs = eval(hcrs)
        print(cv_p)
        print(hcrs)
        
        if cv2.waitKey(20000) == "q":
            break

    client.close()
    server.close()

if __name__ == "__main__":
    main()
