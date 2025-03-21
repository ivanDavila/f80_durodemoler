import pandas as pd

import torch

#..... Tracker modules......
# from f80.yolov7.segment.sort_count import *
import numpy as np
import cv2
#...........................

from f80.yolov7.models.common import DetectMultiBackend
from f80.yolov7.utils.general import check_img_size, non_max_suppression
from f80.yolov7.utils.segment.general import process_mask
# from f80.yolov7.utils.segment.plots import plot_masks
from f80.yolov7.utils.plots import colors

def overlay(image, mask, color, alpha, resize=None):
    """Combines image and its segmentation mask into a single image.
    https://www.kaggle.com/code/purplejester/showing-samples-with-segmentation-mask-overlay

    Params:
        image: Training image. np.ndarray,
        mask: Segmentation mask. np.ndarray,
        color: Color for segmentation mask rendering.  tuple[int, int, int] = (255, 0, 0)
        alpha: Segmentation mask's transparency. float = 0.5,
        resize: If provided, both image and its mask are resized before blending them together.
        tuple[int, int] = (1024, 1024))

    Returns:
        image_combined: The combined image. np.ndarray

    """
    color = color[::-1]
    colored_mask = np.expand_dims(mask, 0).repeat(3, axis=0)
    colored_mask = np.moveaxis(colored_mask, 0, -1)
    masked = np.ma.MaskedArray(image, mask=colored_mask, fill_value=color)
    image_overlay = masked.filled()

    if resize is not None:
        image = cv2.resize(image.transpose(1, 2, 0), resize)
        image_overlay = cv2.resize(image_overlay.transpose(1, 2, 0), resize)

    image_combined = cv2.addWeighted(image, 1 - alpha, image_overlay, alpha, 0)

    return image_combined

class InstSegmYOLOv7:
    def __init__(self, model_path):
        # model_path = 'best.pt'  # model.pt path(s)
        # im_source = r"roca2_rec.jpg"
        # im0 = cv2.imread(im_source)

        # Load gpu
        self.device = torch.device('cuda:0')

        imgsz=(640, 640)  # inference size (height, width)

        dnn=False  # use OpenCV DNN for ONNX inference

        self.model = DetectMultiBackend(
            model_path, 
            device=self.device, 
            dnn=dnn, fp16=False
            )
        
        stride, pt = self.model.stride, self.model.pt
        imgsz = check_img_size(imgsz, s=stride)  # check image size

        bs = 1  # batch_size
        self.model.warmup(imgsz=(1 if pt else bs, 3, *imgsz))  # warmup

    def predict(self, source_im: np.array, conf_thres, iou_thres, max_det):
        print("esta madre si funciono")
        with torch.no_grad():
            dw = source_im.shape[1]
            dh = source_im.shape[0]

            pre_image = self.preprocess_img(source_im)
            # Lo convertirmos a un tensor de torch
            image = torch.from_numpy(pre_image).to(self.device)
            # Lo normalizamos (llevar los valores del rango 0 - 255 a 0 - 1)
            image /= 255
            image = (image.half() 
                        if self.model.fp16 
                        else image.float() ) # uint8 to fp16/32
            # im /= 255  # 0 - 255 to 0.0 - 1.0
            if len(image.shape) == 3:
                image = image[None]  # expand for batch dim

            # Inference
            visualize = False
            augment=False  # augmented inference
            pred, out = self.model(
                image, 
                augment=augment, 
                visualize=visualize
                )
            
            proto = out[1]

            classes=None  # filter by class: --class 0, or --class 0 2 3
            agnostic_nms=False  # class-agnostic NMS

            pred = non_max_suppression(
                pred, 
                conf_thres, 
                iou_thres, 
                classes, 
                agnostic_nms, 
                max_det=max_det, 
                nm=32
                )

            det = pred[0]  # per image
            object_detect = len(det) > 0
            im_masks = None
            rslt = None
            print("esta madre si funciono")

        if object_detect:
            masks = process_mask(
                proto[0], 
                det[:, 6:], 
                det[:, :4], 
                image.shape[2:], 
                upsample=True
                )  # HWC
        
            
            
            #filtramos las bandas
            clss  = det[:,5].byte().cpu().numpy()
            is_rock = clss == 0 #clasificacion de roca es 0

            m = masks.byte().cpu().numpy()
            m_rock = m[is_rock]

            #reajustamos la imagen al tamaño original
            segment = [cv2.resize(
                mks, (dw, dh), 
                interpolation = cv2.INTER_LINEAR
                ) for mks in m_rock]
        
            retc_ar = []
            area_ar = []
            # imag_cp = im0.copy()
            print(len(segment))

            # Inicializamos imagen para el Overlay
            imag_bin = np.zeros(source_im.shape[:2], dtype='uint8')

            for segm in segment:
                # if i == 0:
                #Capturamos todos las detecciones en una sola imagen
                segm[segm > 0] = 255 
                imag_bin = cv2.bitwise_or(imag_bin, segm)

                cont, _ = cv2.findContours(
                    segm, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
                    )
                
                cnt = [cv2.contourArea(cnt) for cnt in cont]
                max_index = cnt.index(max(cnt))

                area = cv2.contourArea(cont[max_index])
                rect = cv2.minAreaRect(cont[max_index])
                
                retc_ar.append(rect[1])
                area_ar.append(area)

            overlay_image = overlay(source_im, imag_bin, (255, 0, 0), 0.5)
            
            if len(segment) >= 0:
                rslt_ell_df = self.cum_ellipsoid(retc_ar)
    
            return object_detect, overlay_image, rslt_ell_df
            
        raise Exception("no object detected")

    def cum_ellipsoid(self, best_fit_rectangle):
        ell_ar = [[max(ejes)*0.4879, min(ejes)*0.4879] for ejes in best_fit_rectangle]
        ell_df = pd.DataFrame(ell_ar, columns=["eje_M", "eje_m"])
        ell_df["ell_vol"] = 4/3 * np.pi * (ell_df["eje_M"])/2 * np.power(ell_df["eje_m"]/2, 2)

        ell_df_sort = ell_df.sort_values("eje_m")
        # ell_df_sort.reset_index(inplace=True)
        histvalues_vol = ell_df_sort["ell_vol"] / ell_df_sort["ell_vol"].sum()*100
        cumulative_vol = np.cumsum(histvalues_vol)
        ell_df_sort["cum_vol"] = cumulative_vol

        return ell_df_sort
    
    def cum_sphere(self, area_ar):
        area_sort = np.sort(area_ar)
        diam = np.power(area_sort, 0.5) * 0.4879
        esf_ar = 4/3 * np.pi * np.power(diam/2, 3)

        hist_esf_vol = esf_ar / esf_ar.sum()*100
        cum_esf_vol = np.cumsum(hist_esf_vol)

        return diam, cum_esf_vol

    def preprocess_img(self, im_source):
        """
        Se adecua la imagen para poderla incorporarla al gpu.
        In:
            im_source -> Imagen BGR de N x M pxls
        Out:
            im_result -> imagen RGB de 640 x 640 pxls
        """
        image = im_source.copy()
        # Convertir de BGR a RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Meterle el padding y hacerle resize
        image = cv2.resize(
            image, (640, 640), 
            interpolation = cv2.INTER_LINEAR
            )
        # Cambiar el orden de las dimensiones para tener (C, H, W)
        image = image.transpose((2, 0, 1))
        # Le expandimos una dimension para tener el batch size (B, C, H, W)
        image = np.expand_dims(image, 0)
        # Lo convierte en una matriz contigua en la memoria
        image = np.ascontiguousarray(image)
        # Lo cambia de tipo a float de 16 bits
        im_result = image.astype(np.float16)

        return im_result

if __name__ == "__main__":
    import time
    
    source = r"roca2_rec.jpg"
    model_path = 'best.pt'
    image = cv2.imread(source)
    model = InstSegmYOLOv7(model_path)

    conf_thres=0.25  # confidence threshold
    iou_thres=0.45  # NMS IOU threshold
    max_det=1000  # maximum detections per image

    obj_dete, image_rslt, cum_rslt = model.predict(image, 
                                                   conf_thres, 
                                                   iou_thres, 
                                                   max_det)
    
    cv2.imshow("result", image_rslt)
    cv2.waitKey(0)