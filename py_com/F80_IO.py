"""Modulo para F80Meter enfocado en la Lectura/Escritura y Conversion de Datos (Tipos de Dato de Python a Palabras (16-bit) de ModbusTCP"""

from pyModbusTCP.client import ModbusClient
import pyModbusTCP.utils

class F80_MBTCP_Client:
    def __init__(self):
        self.host_address = "192.168.1.1"
        self.port = 502
        self.remote_client = ModbusClient(timeout=1)
        self.remote_client.host(self.host_address)
        self.remote_client.port(self.port)

    def setHostAddress(self, ip_address:str = "192.168.1.1") -> None:
        """
        Ajuste de la Direccion IP del Servidor de ModbusTCP con el
        cual se busca establecer conexion.

        Args:

            ip_address (int): Direccion IPv4/IPv6 donde se ubica el
            host de ModbusTCP

        Returns: None

        """
        self.host_address = ip_address
        self.remote_client.host(self.host_address)

    def setPort(self, port:str = 502) -> None:
        """Ajuste del Puerto del Firewall a traves del cual se busca establecer conexion con el Servidor de ModbusTCP

            Args:

                port (int): Numero del puerto a utilizar para comunicacion via ModbusTCP

            Returns: None

        """
        self.port = port
        self.remote_client.port(self.port)

    def readDINT(self, addr_offset:int = 0, div_by:float = 1.0, little_endian:bool = True) -> float:
        """Adquiere un dato de tipo Doble Entero (DINT/32-bit) alojado en dos registros (16-bit) de ModbusTCP contiguos

            Args:

                addr_offset (int): Posicion del Registro de Retencion inicial (40000-49999) del cual se leera. Se obtiene el valor
                conjunto de 32-bit leido de los registros en el [offset] y [offset+1]. Eg. Si addr_offset=1, se leera de las posiciones
                40001 y 40002.

                div_by (float): Valor numerico entre el cual dividir el valor conjunto de los Registros de Retencion

                little_endian (bool): Indica el orden de significancia con el cual se concatenaran las palabras (16-bit) entrantes.
                Eg. Si addr_offset=20 y little_endian=True, la palabra con menor significancia sera la del registro 20 y la de
                mayor significancia sera la del registro 21. Si little_endian=False, se tomara la palabra del registro 21 con menor significancia
                y la del 20 con mayor significancia.

            Returns: Valor del DINT alojado en los registro de ModbusTCP (float)

        """
        try:
            if not self.remote_client.is_open():
                if not self.remote_client.open():
                    print(f"Unable to connect Remote Client to Server on {self.host_address}:{self.port}")
            if self.remote_client.is_open():
                if little_endian:
                    data = (self.remote_client.read_holding_registers(addr_offset)[0]) + (65536 * self.remote_client.read_holding_registers(addr_offset+1)[0])
                else:
                    data = (self.remote_client.read_holding_registers(addr_offset+1)[0]) + (65536 * self.remote_client.read_holding_registers(addr_offset)[0])
                #print(data)
                data /= div_by
                #print(data)
                return data
        except Exception as e:
            print(e)


    def writeDINT(self, data:float = 0, addr_offset:int = 0, mult_by:int = 1, little_endian:bool = True) -> None:
        """Convierte un dato de tipo Float a uno de tipo Doble Entero (DINT/32-bit) para despues alojarlo en dos registros (16-bit) de ModbusTCP contiguos

            Args:

                data (float): Valor numerico a procesar y escribir en los Registros de Retencion de ModbusTCP

                addr_offset (int): Posicion del Registro de Retencion inicial (40000-49999) al cual se escribira. Se divide el valor
                entero de 32-bit para posteriormente alojarlo respectivamente en los registros en el [offset] y [offset+1]. Eg. Si addr_offset=1, se
                escribira a las posiciones 40001 y 40002.

                mult_by (int): Valor numerico por el cual multiplicar el valor del argumento 'data' antes de ser separado en Palabras de 16-bit

                little_endian (bool): Indica el orden de significancia con el cual se concatenaran las palabras (16-bit) entrantes.
                Eg. Si addr_offset=20 y little_endian=True, la palabra con menor significancia sera la del registro 20 y la de
                mayor significancia sera la del registro 21. Si little_endian=False, se tomara la palabra del registro 21 con menor significancia
                y la del 20 con mayor significancia.

            Returns: None

        """
        try:
            if not self.remote_client.is_open():
                if not self.remote_client.open():
                    print(f"Unable to connect Remote Client to Server on {self.host_address}:{self.port}")
            if self.remote_client.is_open():
                #print(data)
                data = int(data * mult_by)
                #print(data)
                split_data = pyModbusTCP.utils.long_list_to_word([data],big_endian=False)
                #print(split_data)
                if little_endian:
                    self.remote_client.write_single_register(addr_offset, split_data[0])
                    self.remote_client.write_single_register(addr_offset+1, split_data[1])
                else:
                    self.remote_client.write_single_register(addr_offset+1, split_data[0])
                    self.remote_client.write_single_register(addr_offset, split_data[1])

        except Exception as e:
            print(e)

