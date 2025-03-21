from f80 import Fifo
from time import sleep, time
from .errorManager import errorManager
from py_com import F80_MBTCP_Client

class ModbusThread:
    def __init__(self, parent, queue):
        #inicilizacion de comunicacion Modbus TCP
        self.parent = parent
        mean_size = 10
        self.SPEED_CONVYR_fifo = Fifo(mean_size)
        self.TPH_Mineral_fifo = Fifo(mean_size)
        self.NVL_CAJON_fifo = Fifo(mean_size)
        self.POWER_KW_fifo = Fifo(mean_size)
        self.WATER_MILL_fifo = Fifo(mean_size)
        self.BOMBA_CAJON_A_fifo = Fifo(mean_size)
        self.BOMBA_CAJON_B_fifo = Fifo(mean_size)
        self.PWR_BOMBA_CAJON_A_fifo = Fifo(mean_size)
        self.PWR_BOMBA_CAJON_B_fifo = Fifo(mean_size)

        self.fifofull = False
        self.com_loop(queue)

    def com_loop(self, queue):

        readclient = F80_MBTCP_Client()
        readclient.setHostAddress("192.168.137.30")
        readclient.setPort(502)

        while True:
            try:
                #leer el valor de modbus cada segundo, almacenamiento en su respectivo fifo
                start = time()
                data = readModbus(readclient)
                end = time()
                mssg1= f"readModbus() data: {data}"
                mssg2 = f"readModbus() time: {end-start}"
                id_none = [val is None for val in data.values()]
                #print("id_none: %s" % any(id_none))
                #if any(id_none):
                #    sleep(1)
                #    print("none detected")
                #    continue

                self.SPEED_CONVYR_fifo.append(data['SPEED_CONVYR'])
                self.TPH_Mineral_fifo.append(data['TPH_Mineral'])
                self.NVL_CAJON_fifo.append(data['NVL_CAJON'])
                self.POWER_KW_fifo.append(data['POWER_KW'])
                self.WATER_MILL_fifo.append(data['WATER_MILL'])
                self.BOMBA_CAJON_A_fifo.append(data['BOMBA_CAJON_A'])
                self.BOMBA_CAJON_B_fifo.append(data['BOMBA_CAJON_B'])
                self.PWR_BOMBA_CAJON_A_fifo.append(data['PWR_BOMBA_CAJON_A'])
                self.PWR_BOMBA_CAJON_B_fifo.append(data['PWR_BOMBA_CAJON_B'])
                self.fifofull = self.SPEED_CONVYR_fifo.is_full()

                SPEED_CONVYR_mean       =sum(self.SPEED_CONVYR_fifo)       /self.SPEED_CONVYR_fifo.maxlen
                TPH_Mineral_mean        =sum(self.TPH_Mineral_fifo)        /self.TPH_Mineral_fifo.maxlen
                NVL_CAJON_mean          =sum(self.NVL_CAJON_fifo)          /self.NVL_CAJON_fifo.maxlen
                POWER_KW_mean           =sum(self.POWER_KW_fifo)           /self.POWER_KW_fifo.maxlen
                WATER_MILL_mean         =sum(self.WATER_MILL_fifo)         /self.WATER_MILL_fifo.maxlen
                BOMBA_CAJON_A_mean      =sum(self.BOMBA_CAJON_A_fifo)      /self.BOMBA_CAJON_A_fifo.maxlen
                BOMBA_CAJON_B_mean      =sum(self.BOMBA_CAJON_B_fifo)      /self.BOMBA_CAJON_B_fifo.maxlen
                PWR_BOMBA_CAJON_A_mean  =sum(self.PWR_BOMBA_CAJON_A_fifo)  /self.PWR_BOMBA_CAJON_A_fifo.maxlen
                PWR_BOMBA_CAJON_B_mean  =sum(self.PWR_BOMBA_CAJON_B_fifo)  /self.PWR_BOMBA_CAJON_B_fifo.maxlen

                ModbusOUT = {
                    'SPEED_CONVYR'      : SPEED_CONVYR_mean,
                    'TPH_Mineral'       : TPH_Mineral_mean,
                    'NVL_CAJON'         : NVL_CAJON_mean,
                    'POWER_KW'          : POWER_KW_mean,
                    'WATER_MILL'        : WATER_MILL_mean,
                    'BOMBA_CAJON_A'     : BOMBA_CAJON_A_mean,
                    'BOMBA_CAJON_B'     : BOMBA_CAJON_B_mean,
                    'PWR_BOMBA_CAJON_A' : PWR_BOMBA_CAJON_A_mean,
                    'PWR_BOMBA_CAJON_B' : PWR_BOMBA_CAJON_B_mean
                }

                #self.parent.log("modbus: %s" % self.SPEED_CONVYR_fifo)

                if queue.full():
                    queue.get()
                    #print("queue lleno, se borrara primer dato")

                queue.put([self.fifofull, ModbusOUT, mssg1, mssg2], block=False)
                sleep(1)
                #raise Exception("error indusido")
            except Exception as e:
                self.parent.log("Error: %s" % e)
                errorManager(e)
                print(e)

def readModbus(client):
    ModbusOUT = {
        'SPEED_CONVYR'      : client.readDINT(98, 100, False),
        'TPH_Mineral'       : client.readDINT(100, 10, False),
        'NVL_CAJON'         : client.readDINT(102, 100, False),
        'POWER_KW'          : client.readDINT(104, 10, False),
        'WATER_MILL'        : client.readDINT(106, 100, False),
        'BOMBA_CAJON_A'     : client.readDINT(110, 100, False),
        'BOMBA_CAJON_B'     : client.readDINT(112, 100, False),
        'PWR_BOMBA_CAJON_A' : client.readDINT(114, 100, False),
        'PWR_BOMBA_CAJON_B' : client.readDINT(116, 100, False)
    }
    return ModbusOUT

def writeModbus(client, register, dataset):
    #enviar variables de DCS
        for data, i in enumerate(dataset):
            client.writeDINT(data, register[i], 100, False)
