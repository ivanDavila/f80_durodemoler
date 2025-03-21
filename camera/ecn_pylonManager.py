from pypylon import pylon
#import cv2
#from datetime import datetime
#from time import sleep

class ecn_pylonManager:
    def __init__(self, pfs_file):
        # conecting to the first available camera
        self.camera = pylon.InstantCamera(
            pylon.TlFactory.GetInstance().CreateFirstDevice())
        
        self.load_pfs(pfs_file)

        # Grabing Continusely (video) with minimal delay
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
        self.converter = pylon.ImageFormatConverter()

        # converting to opencv bgr format
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    def capture_image(self):
        try:
            if self.camera.IsGrabbing():
                grabResult = self.camera.RetrieveResult(
                    5000, pylon.TimeoutHandling_ThrowException)

                if grabResult.GrabSucceeded():
                    
                    image = self.converter.Convert(grabResult)
                    img = image.GetArray()

                    grabResult.Release()
                    return img

        except Exception as e:
            raise Exception("Camera Desconected")
    
    def close(self):
        self.camera.StopGrabbing()
    
    def load_pfs(self, pfs_dir) -> None:
        """
        Cargar pfs.
            -cam_info informacion de camara
            -pfs_dir: director de folder pfs

        """
        #inicializar acamara con cam_info
        self.camera.Open()
        pylon.FeaturePersistence.Load(pfs_dir, self.camera.GetNodeMap())
        # print("se creo archivo pfs: '%s'" % (self.pfs_file))
        #cerrar configuracion de camara
        self.camera.Close()

if __name__ == "__main__":
    import cv2
    try:
        mycam = ecn_pylonManager()
        while True:
            image = mycam.capture_image()
            image = image[259:2741,:]
            image = cv2.resize(image, (1650, 1000), cv2.INTER_CUBIC)
            cv2.imshow("image", image)
            cv2.waitKey(1)

    except Exception as e:
        print(e)

    finally:
        # Releasing the resource    
        mycam.close()
        print("camara se detuvo correctamente")
        #cv2.destroyAllWindows()