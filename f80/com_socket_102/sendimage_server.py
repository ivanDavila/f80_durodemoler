import socket
import pickle
import struct
import numpy as np
# from PIL import Image
from time import sleep

class ComError(Exception):
    pass

class SOCKET_SERVER:
    def __init__(self, host, port, package_size = 1024):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(10)
        self.package_size = package_size

    def start_server(self):
        self.conn, self.addr = self.server_socket.accept()
        data = b""
        payload_size = struct.calcsize(">L")
    
    
    def com_server(self, sdata):
        #print("wait for response")
        # receive data stream. it won't accept data packet greater than 1024 bytes
        dataclient = self.conn.recv(self.package_size).decode()
        if not dataclient:
            # if data is not received break
            raise ComError("no hay conexion con cliente")
    

        #print("recieved message: %s" % dataclient)

        data = pickle.dumps(sdata, 0)
        size = len(data)
        self.conn.sendall(struct.pack(">L", size) + data)
        # print("file: " + fle)
        #print("size: %i" % size)
        # sleep(1)


if __name__ == '__main__':
    from PIL import Image
    import os, sys

    #initialice images files
    archvs = os.path.abspath(os.path.dirname(sys.argv[0]))
    archvs = archvs.split('\\')
    archvs = '/'.join(archvs[:-2]) + '/data/imgs'
    # archvs = '/'.join(archvs) + '/data/imgs'
    myfiles = os.listdir(archvs)
    imfile = ['{}/{}'.format(archvs, x) for x in myfiles if '.jpg' or '.png' in x]
    imfile.sort()

    #initialize comunication
    # host = socket.gethostname()
    # port = 5000
    host = "192.168.10.10"
    port = 65432

    server = SOCKET_SERVER(host, port)

    while True:
        try:

            server.start_server()

            while True:
                for fle in imfile:
                    image = Image.open(fle)
                    message = np.asarray(image)
                    server.com_server(message)
                    # raise("error inducido por el usuario")

        except Exception as e:
            server.conn.close()
            print(e)

        except ConnectionResetError as e:
            server.conn.close()
            print(e)