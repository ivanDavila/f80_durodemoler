# -----------------------------------------------------------------------------
# Copyright (c) 2021, Lucid Vision Labs, Inc.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -----------------------------------------------------------------------------

import os  # os.getcwd()
import time
from pathlib import Path

import numpy as np  # pip install numpy
from PIL import Image as PIL_Image  # pip install Pillow

from arena_api.system import system
from datetime import datetime

def create_devices_with_tries():
    """
    This function waits for the user to connect a device before raising
    an exception
    """

    tries = 0
    tries_max = 6
    sleep_time_secs = 10
    while tries < tries_max:  # Wait for device for 60 seconds
        devices = system.create_device()
        if not devices:
            #print(
                #f'Try {tries+1} of {tries_max}: waiting for {sleep_time_secs} '
                #f'secs for a device to be connected!')
            for sec_count in range(sleep_time_secs):
                time.sleep(1)
                #print(f'{sec_count + 1 } seconds passed ',
                #      '.' * sec_count, end='\r')
            tries += 1
        else:
            #print(f'Created {len(devices)} device(s)')
            return devices
    else:
        raise Exception(f'No device found! Please connect a device and run '
                        f'the example again.')


class TRITON_CAM:
    def __init__(self):
        # Create a device
        devices = create_devices_with_tries()
        self.device = devices[0]
        #print(f'Device used in the example:\n\t{self.device}')

        # Get device stream nodemap
        tl_stream_nodemap = self.device.tl_stream_nodemap

        # Enable stream auto negotiate packet size
        tl_stream_nodemap['StreamAutoNegotiatePacketSize'].value = True

        # Enable stream packet resend
        tl_stream_nodemap['StreamPacketResendEnable'].value = True

        # Get/Set nodes -----------------------------------------------------------
        #nodes = self.device.nodemap.get_node(['Width', 'Height', 'PixelFormat'])

        # Nodes
        #print('Setting Width to its maximum value')
        #nodes['Width'].value = nodes['Width'].max

        #print('Setting Height to its maximum value')
        #height = nodes['Height']
        #height.value = height.max

        # Set pixel format to Mono8, most cameras should support this pixel format
        #pixel_format_name = 'RGB8'
        #print(f'Setting Pixel Format to {pixel_format_name}')
        #nodes['PixelFormat'].value = pixel_format_name

        # Grab and save an image buffer -------------------------------------------
        print('Starting stream')

        self.device.start_stream()
        print("device start")
    
    def camera_capture(self):
        print('Converting image buffer to a numpy array')
        image_buffer = self.device.get_buffer(timeout = 10000)
        image_only_data = None
        if image_buffer.has_chunkdata:
            # 8 is the number of bits in a byte
            bytes_pre_pixel = int(image_buffer.bits_per_pixel / 8)

            image_size_in_bytes = image_buffer.height * \
                image_buffer.width * bytes_pre_pixel

            image_only_data = image_buffer.data[:image_size_in_bytes]
            #print("image has chunkdata")
        else:
            image_only_data = image_buffer.data

        nparray = np.asarray(image_only_data, dtype=np.uint8)
        # Reshape array for pillow
        nparray_reshaped = nparray.reshape((
            image_buffer.height,
            image_buffer.width,
            3
        ))

        self.device.requeue_buffer(image_buffer)
        return nparray_reshaped

    def adquire_image(self, npath):
        #print('Grabbing an image buffer')
        # Optional args
        image_buffer = self.device.get_buffer(timeout = 10000)
        #print(f' Width X Height = '
        #    f'{image_buffer.width} x {image_buffer.height}')

        # To save an image Pillow needs an array that is shaped to
        # (height, width). In order to obtain such an array we use numpy
        # library
        print('Converting image buffer to a numpy array')

        # Buffer.pdata is a (uint8, ctypes.c_ubyte)
        # Buffer.data is a list of elements each represents one byte. Therefore
        # for Mono8 each element represents a pixel.

        #
        # Method 1 (from Buffer.data)
        #
        # dtype is uint8 because Buffer.data returns a list or bytes and pixel
        # format is also Mono8.
        # NOTE:
        # if 'ChunkModeActive' node value is True then the Buffer.data is
        # a list of (image data + the chunkdata) so data list needs to be
        # truncated to have image data only.
        # can use either :
        #  - device.nodemap['ChunkModeActive'].value   (expensive)
        #  - buffer.has_chunkdata                 (less expensive)
        image_only_data = None
        if image_buffer.has_chunkdata:
            # 8 is the number of bits in a byte
            bytes_pre_pixel = int(image_buffer.bits_per_pixel / 8)

            image_size_in_bytes = image_buffer.height * \
                image_buffer.width * bytes_pre_pixel

            image_only_data = image_buffer.data[:image_size_in_bytes]
            #print("image has chunkdata")
        else:
            image_only_data = image_buffer.data

        nparray = np.asarray(image_only_data, dtype=np.uint8)
        # Reshape array for pillow
        nparray_reshaped = nparray.reshape((
            image_buffer.height,
            image_buffer.width,
            3
        ))

        #
        # Method 2 (from Buffer.pdata)
        #
        # A more general way (not used in this simple example)
        #
        # Creates an already reshaped array to use directly with
        # pillow.
        # np.ctypeslib.as_array() detects that Buffer.pdata is (uint8, c_ubyte)
        # type so it interprets each byte as an element.
        # For 16Bit images Buffer.pdata must be cast to (uint16, c_ushort)
        # using ctypes.cast(). After casting, np.ctypeslib.as_array() can
        # interpret every two bytes as one array element (a pixel).
        #
        # Code:
        '''
        nparray_reshaped = np.ctypeslib.as_array(
        image_buffer.pdata,
        (image_buffer.height, image_buffer.width))
        '''
        #

        # Save image
        print('Saving image')
        #png_name = f'from_{pixel_format_name}_to_png_with_pil.png'
        currentDT = datetime.now()
        filename = npath
        imagefile = "%s/%.2d%.2d%.2d_%.2d%.2d%.2d.png" % (filename, currentDT.year, currentDT.month, currentDT.day, currentDT.hour, currentDT.minute, currentDT.second)
        
        png_array = PIL_Image.fromarray(nparray_reshaped)
        png_array.save(imagefile)
        print('Saved image path is: %s' % imagefile)

        self.device.requeue_buffer(image_buffer)

    def close(self):
        self.device.stop_stream()
        print('Stream stopped')
        system.destroy_device()
        print('Destroyed all created devices')
        print('\nExample finished successfully')


if __name__ == '__main__':
    import cv2
    try:
        print('\nWARNING:\nTHIS EXAMPLE MIGHT CHANGE THE DEVICE(S) SETTINGS!')
        print('\nExample started\n')
        tcam = TRITON_CAM()
        npath = "/media/ecnjetson/ecnsc"
        while tcam.device.is_connected():
            image = tcam.camera_capture()
            #cv2.imshow("hello",image)
            #cv2.waitKey(1000)

    finally:
        tcam.close()