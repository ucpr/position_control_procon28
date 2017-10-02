import socket
from datetime import datetime

address = ('localhost', 5000)
max_size = 1000

print('Start client', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)


def main():
    for i in range(10):
        data = client.recv(max_size)
        print(data)

    client.close()
    print('close client', datetime.now())


if __name__ == "__main__":
    main()
