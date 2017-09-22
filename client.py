import socket
from datetime import datetime
import cv2
import cv_position
import hcrs_position

cap = cv2.VideoCapture(0)
server_address = ('localhost', 5000)
max_size = 4096


def main():
    print('Starting the client at', datetime.now())
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        x, z = cv_position.position(cap)
        y = hcrs_position.position()
        cv_bytes = (str(x) + " " + str(z)).encode("utf-8")
        hcrs_byte = str(y).encode("utf-8")

        client.sendto(cv_bytes, server_address)
        client.sendto(hcrs_byte, server_address)

        if cv2.waitKey(2000) == "q":
            break

    client.close()
    cap.release()

if __name__ == "__main__":
    main()
