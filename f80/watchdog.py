from threading import Timer
from time import sleep

class Watchdog:
    def __init__(self, name = "",  
                 timeout = 60, userHandler=None):  
        # timeout in seconds
        self.name = name
        self.timeout = timeout
        self.handler = (userHandler if userHandler 
                        is not None else self.defaultHandler
                        )
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def reset(self):
        self.timer.cancel()
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def stop(self):
        self.timer.cancel()

    def defaultHandler(self):
        pass

class WatchdogList(list):
    """
    lista de watchdogs.
    
    """
    def create_watchdog(self, name = "", timeout = 30) -> Watchdog:
        """
        crea un elemento watchdog.
        """
        watchdog = Watchdog(name = name, timeout = timeout)
        self.append(watchdog)
        return watchdog

    def print_watchdog(self) -> str:
        """
        Imprime watchdogs activos.
        """
        return [wd.name for wd in self]
    
    def washa_watchdog(self) -> None:
        """
        Se lee si algun watchdog esta timeoout.

        """
        for watchdog in self:
            if not watchdog.timer.isAlive():
                raise WatchdogTimeout(watchdog.name)
    
    def find_watchdog(self, name) -> Watchdog:
        """
        Busca watchdog en lista
        
        """
        for watchdog in self:
            if watchdog.name == name:
                return watchdog

        raise notFounded(name)

    def stop_watchdogList(self):
        """
        Detiene todos los watchdog de la lista
        
        """
        for wd in self:
            wd.stop()

class WatchdogTimeout(Exception):
    """Exception raised for errors timeout.

    Attributes:
    
        watchdog_name -- name of the watchdog timeout

    """

    def __init__(self, watchdog_name):
        self.watchdog_name = watchdog_name
        self.message = "Watchdog clock in %s timeout" % self.watchdog_name
        super().__init__(self.message)

class notFounded(Exception):

    def __init__(self, name):
        self.name = name
        self.message = "'%s' no found" % self.name
        super().__init__(self.message)

if __name__ == "__main__":
    wd_list = watchdog_list()
    wd_01 = wd_list.create_watchdog(name="wd_01", timeout=5)
    wd_02 = wd_list.create_watchdog(name="wd_02", timeout=1)
    wd_03 = wd_list.create_watchdog(name="wd_03", timeout=10)

    wd_00 = wd_list.find_watchdog(name="wd_03")

    print(wd_list.print_watchdog())
    try:
        while True:
            sleep(4)
            # wd_01.reset()
            # wd_02.reset()
            # wd_02.reset()
            wd_list.washa_watchdog()
            print("esto se ejecuto")

    except Exception as e:
        print(e)