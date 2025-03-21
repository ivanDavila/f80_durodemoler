# from camera.ecn_arenaMngr import TRITON_CAM
from camera.ecn_pylonManager import ecn_pylonManager
# from ecn_pylonManager import ecn_pylonManager
# from f80.errorManager import errorManager
from time import time, sleep

# Para esta prueba vamos a quitar el manejador de errores
# cameraHandle(parent, queue, delay)

def cameraHandle(queue, delay):
    """
    Programa para manejar camaras,
        queue: donde se comparten las imagenes
        time: delay; tiene que ser mas de lo que se tarda la captura 
        (2 segundos).

    """
 
    try:
        while True:
            print('\nWARNING:\nTHIS EXAMPLE MIGHT CHANGE THE DEVICE(S) SETTINGS!')
            print('\nExample started\n')
            tcam = ecn_pylonManager()
            npath = "/media/ecnjetson/ecnsc"
            while tcam.camera.is_connected():
                    start_time = time()
                    image = tcam.capture_image()
                    if queue.full():
                        queue.get()
                        print("queue lleno, se borrara primer dato")

                    queue.put(image, block=True)
                    elapsed_time = time() - start_time
                    print("adqusition time ", elapsed_time)
                    sleep(delay)

    except Exception as e:
        print(e)
        # errorManager(parent, e)
            
    finally:
        tcam.close()

def cameraHandle_offline(queue, delay):
    """
    Programa para manejar camaras,
        queue: donde se comparten las imagenes
        time: delay; tiene que ser mas de lo que se tarda la captura (2 segundos)"""

    try:
        tcam = ecn_pylonManager()
        npath = "/media/ecnjetson/ecnsc"
        while tcam.device.is_connected():
                start_time = time()
                image = tcam.camera_capture()
                #Comunicacion a Computadora de visualizacion via socket
                if queue.full():
                    queue.get(False, timeout=1)

                queue.put(image, block=True)

    except Exception as e:
        print(e)
                
    finally:
        tcam.close()

if __name__ == "__main__":
    import cv2
    from threading import Thread
    from queue import Queue, Empty
    try:
        #empezar thread de camara
        delay = 1
        cameraqueue = Queue(maxsize=1)
        servercom = Thread(target=cameraHandle, 
                            args=(cameraqueue, 
                                    delay))
        servercom.daemon = True
        servercom.start()
        while True:
            try:
                image = cameraqueue.get(True, timeout=5)
                image = image[259:2741,:]
                image = cv2.resize(image, (1650, 1000), cv2.INTER_CUBIC)
                cv2.imshow("image", image)
                cv2.waitKey(1)
            except Empty as e:
                print("se activa el timeout falio ferga")
                print(e)

    except Exception as e:
        print(e)