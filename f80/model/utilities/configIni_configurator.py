import json

class ConfigIni_Configurator():
    def __init__(self, configini_file = "config.ini"):
        self.configini_file = configini_file

    def read_config(self):
        try:
            data_dir = {}
            with open(self.configini_file, 'r') as config:
                data_info = config.read()
                data_dir = json.loads(data_info)
                # print(data_dir)
                # self.print_status("Loding config.ini successfully")
            return data_dir['configuracion']

        except Exception as e:
            # self.print_status("Error: %s" % e)
            print("Error: %s" % e)
            return {}
    
    # def update_config(self):
    #     try:
    #         """
    #         Se actualiza la el registro de configuracion 'self.configlist' con los inputs de frontend
    #         """
    #         h, _, _ = self.image.shape
    #         self.configlist['img_path'] = self.lineEdit_imagpath.text()
    #         self.configlist['model_path'] = self.lineEdit_modelpath.text()
    #         self.configlist['lookup_path'] = self.lineEdit_lookuppath.text()
    #         self.configlist['windowing'] = [self.spinBox_xwin.value(), self.spinBox_ywin.value()]
    #         self.configlist['origins'] = [self.spinBox_xorigin.value(), self.spinBox_yorigin.value()]
    #         self.configlist['offset'] = self.spinBox_overlapping.value()
    #         self.configlist['NumBoxes'] = [self.spinBox_xNBoxes.value(), self.spinBox_yNBoxes.value()]
    #         self.configlist['ImgExtract_Point1'] = [self.spinBox_extract1_x.value(), self.spinBox_extract1_y.value()]
    #         self.configlist['ImgExtract_Point2'] = [self.spinBox_extract2_x.value(), self.spinBox_extract2_y.value()]
    #         self.configlist['mirror'] = self.checkBox_mirror.isChecked()
    #         self.configlist['lookup_table_check'] = self.checkBox_lookuptable.isChecked()

    #         window = self.configlist['windowing']
    #         offset = self.configlist['offset']
    #         origin = self.configlist['origins']

    #         self.loadLookUpTable_Txt(self.configlist['lookup_path'])

    #         #CAMBIAR SISTEMA DE ESCALA LATERAL; Convertir de escala Matplotlib a PXL
    #         self.preprocess_image()
    #         imgscaleH, _, _ =  self.preprocessed_image.shape
    #         RectImages = []
            
    #         for xNBox in range(self.configlist['NumBoxes'][0]):
    #             for yNBox in range(self.configlist['NumBoxes'][1]):               
    #                 point1 = [xNBox*(window[0] - offset) + origin[0],
    #                             imgscaleH - (yNBox*(window[1] - offset) + origin[1])]
    #                 point2 = [xNBox*(window[0] - offset) + origin[0] + window[0],
    #                             imgscaleH - (yNBox*(window[1] - offset) + origin[1] + window[1])]
    #                 RectImages.append([point1, point2])
    #         self.configlist['RectImages'] = RectImages

if __name__ == "__main__":
    config_ini = ConfigIni_Configurator()
    data = config_ini.read_config()
    print(data)