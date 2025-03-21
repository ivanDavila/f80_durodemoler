import cv2
import os, sys
import numpy as np


# from sendimage_client import SOCKET_CLIENT
from sendimage_server import SOCKET_SERVER

from socket import gethostname
from PIL import Image

# host = gethostname()
# port = 5000
# cliente = SOCKET_CLIENT(host, port)

#initialice images files
archvs = os.path.abspath(os.path.dirname(sys.argv[0]))
archvs = archvs.split('\\')
archvs = '/'.join(archvs[:-2]) + '/data/imgs'
myfiles = os.listdir(archvs)
imfile = ['{}/{}'.format(archvs, x) for x in myfiles if '.jpg' or '.png' in x]
imfile.sort()

#initialize comunication
host = gethostname()
port = 5000

server = SOCKET_SERVER(host, port)

def socket_server():
    while True:
        try:

            server.start_server()

            while True:
                for fle in imfile:
                    image = Image.open(fle)
                    message = np.asarray(image)
                    server.com_server(message)

        except Exception as e:
            server.conn.close()
            print(e)

        except ConnectionResetError as e:
            server.conn.close()
            print(e)


while True:
    socket_server()