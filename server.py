from datetime import datetime
from time import sleep
import socket
import cv2
import cv_position
import hcrs_position

cap = cv2.VideoCapture(0)
address = ('localhost', 5000)
max_size = 4096


class Server:

    def __init__(self):
        print("waiting...")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(address)
        self.server.listen(5)
        self.client, addr = self.server.accept()
        print('Start server', datetime.now())
        print('At', datetime.now(), self.client, addr)

    def __del__(self):
        self.client.close()
        self.server.close()
        print("close server", datetime.now())

    def run(self):
        """
        Raises
        ------
        BrokenPipeError
            client側がcloseしていた場合
        KeyboardInterrupt
            Ctrl+cなどでプログラムが終了されたら
        """
        while True:
            try:
                x, z = cv_position.position(cap)
                y = hcrs_position.position()
                res = (str(x) + " " + str(z) + " " + str(y)).encode()

                self.client.sendall(res)
                sleep(0.3)

            except BrokenPipeError:
                print("close client")
                print("reconnect...")
                self.__init__()  # また接続を待つ

            except KeyboardInterrupt:
                break

            except:
                """ その他の例外を見てみたいだけなんです... """
                print(__import__("traceback").print_exc())


if __name__ == "__main__":
    s = Server()
    s.run()
