from f80.com_socket_102 import SOCKET_SERVER
from f80 import errorManager


def server_com_loop(queue, 
                    host, 
                    port, 
                    package_size = 1024):
    #initialize comunication
    server = SOCKET_SERVER(host, port, package_size)
    while True:
        try:
            server.start_server()

            while True:                    
                data = queue.get()
                server.com_server(data)
                print("messeage was sended")

        except Exception as e:
            errorManager(e)
            server.conn.close()