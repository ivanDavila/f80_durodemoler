# import cv2
#import io
import socket
import struct
import time
import pickle
from PIL import Image
from time import sleep

class SOCKET_CLIENT:
    def __init__(self, host, port, package_size = 1024):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

        self.data = b""
        self.payload_size = struct.calcsize(">L")
        print("payload_size: {}".format(self.payload_size))

        self.package_size = package_size

    def recieve_mssg(self):
        #mensaje de aperura de cliente
        message = "Ready to recieve data"
        self.client_socket.send(message.encode())

        #recepcion de datos de servidor
        while len(self.data) < self.payload_size:
            print("Recv: {}".format(len(self.data)))
            self.data += self.client_socket.recv(self.package_size)


        print("Done Recv: {}".format(len(self.data)))
        packed_msg_size = self.data[:self.payload_size]
        self.data = self.data[self.payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        print("msg_size: {}".format(msg_size))
        while len(self.data) < msg_size:
            self.data += self.client_socket.recv(self.package_size)
        frame_data = self.data[:msg_size]
        self.data = self.data[msg_size:]

        frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        return frame
        # frame=pickle.loads(frame_data)
        # print("message: '{}'".format(frame))
        # frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

if __name__ == '__main__':
    import cv2
    # host = socket.gethostname()
    # port = 5000
    host = "192.168.10.10"
    port = 65432
    cliente = SOCKET_CLIENT(host, port)

    while True:
        frame = cliente.recieve_mssg()
        cv2.imshow('ImageWindow',frame)
        cv2.waitKey(1)
        
