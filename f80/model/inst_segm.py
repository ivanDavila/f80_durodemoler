import pandas as pd
from ultralytics import YOLO
import cv2
import numpy as np
import math
from scipy.interpolate import interp1d

class YoloModel:
    def __init__(self, model_path) -> None:
        try:
            # Se carga el Modelo YOLOv8
            print("Loading Model %s..." % model_path)
            self.model = YOLO(model_path)

            self.status = "Model weights loaded successfully"
            print(self.status)
            
        except Exception as e:
            print(e)
    
    def Predictor(self, image):

        results = self.model.predict(image, 
                                verbose=False, 
                                conf=0.5, 
                                iou=0.65)
        
        result = results[0]
        
        bol = np.array([], dtype = bool)
        for box in result.boxes:
            class_id = result.names[box.cls[0].item()]
            cords = box.xywh[0].tolist()
            cords = [round(x) for x in cords]
            m_cords = [round(cords[0] + cords[2] / 2), round(cords[1] + cords[3] / 2)]
            conf = round(box.conf[0].item(), 2)
            bol = np.append(bol, class_id == "b")
        
        band_mask = result.masks[~bol]

        rect_list = []
        count = 0
        count_min_3mm = 0

        for i, mks in enumerate(band_mask.data):
            binim = mks.cpu()
            binim = binim.numpy()
            binim = cv2.normalize(
                    binim, 
                    None, 255, 0, 
                    cv2.NORM_MINMAX, 
                    cv2.CV_8U
                    )
            if i == 0:
                rslt_binim = binim.copy()
            else:
                rslt_binim = cv2.bitwise_or(rslt_binim, binim)

            ratio_rock = cv2.countNonZero(rslt_binim)/rslt_binim.size
            perc_rock = ratio_rock*100

        for cntrns in band_mask.xy:
            rect = cv2.minAreaRect(cntrns)
            rect_list.append(rect[1])
            count += 1
            if min(rect[1]) < 3:
                count_min_3mm = count_min_3mm + 1
            
        
        ellips_list = [[
            max(ejes)*0.4879, 
            min(ejes)*0.4879] for ejes in rect_list]
        rect_df = pd.DataFrame(ellips_list, columns=[
            "eje_M",
            "eje_m"]
            )
        rect_df["ell_vol"] = (4/3 * np.pi * (rect_df["eje_M"])/2 
                              * np.power((rect_df["eje_m"])/2, 2))
        ellips_df  = rect_df.sort_values("eje_m")
        histvalues_vol = ellips_df["ell_vol"] / ellips_df["ell_vol"].sum()*100
        cumulative = np.cumsum(histvalues_vol)

        try: 
            psd = interp1d(cumulative.tolist(), ellips_df["eje_m"].tolist())
            Fs = psd([10,20,30,40,50,60,70,80,90])
            Fs = np.append(Fs, max(ellips_df["eje_m"]))
        except Exception as e:
            Fs = np.full(10, 0)
        
        data_result = [Fs, count, count_min_3mm, perc_rock]

        im_result = results[0].plot(conf=True, boxes=False, labels=True)[...,::-1]

        return im_result, data_result


if __name__ == "__main__":
    import cv2 as cv
    import os

    imgs_path = r"C:\Users\Ivan\Documents\Python\ECN-Automation\Instance_Segmentation\data\data_rec_2"
    imgs = [os.path.join(imgs_path, file) for file in os.listdir(imgs_path)]

    images = [cv2.imread(im) for im in imgs]

    model_path = r"C:\Users\Ivan\Documents\Python\ECN-Automation\Instance_Segmentation\models\cl_faja04_v1.pt"
    print("Loading Model %s..." % model_path)
    ecn_model = YoloModel(model_path)

    for image in images:
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        mask = ecn_model.Predictor(image)
        mask = cv.resize(mask, [640, 640])
        cv.imshow("hellow", mask)
        cv.waitKey(0)
    # visualize(image = image, mask = mask[1])