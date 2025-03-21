import datetime
from queue import Queue
from threading import Thread
from time import sleep
from pathlib import Path
from os.path import abspath, dirname
import sys

from f80.config import read_config
# from f80.f80_process import appDir

appDir = Path(abspath(dirname(sys.argv[0])))

class Scheduler():
    def __init__(self, queue:Queue):
        config_path = appDir / "f80" \
            / "scheduler" /"config.json"
        shedule = read_config(config_path)
        scheduler_thread = Thread(
            target = self.schedule_clock, 
            args = (shedule, queue,)
            )
        scheduler_thread.daemon = True
        scheduler_thread.start()

    def schedule_clock(self, schedule:dict, queue:Queue):
        while True:
            time_now = datetime.datetime.now()
            for key in schedule.keys():
                #el primer elemento es el que dice 
                #cuendo se resetea todos los aquires
                if key == "main_shedule":
                    current_day_str = schedule[key]["actual_day"]
                    current_day = datetime.datetime.strptime(
                        current_day_str, "%Y-%m-%d")
                    #este se triguea cuando cambia el dia
                    if current_day.day != time_now.day:
                        #todos los aquired cambian a False, excepto del schedule_main
                        for k in list(schedule.keys())[1:]:
                            schedule_time = [datetime.datetime.strptime(
                                t1, "%H:%M:%S") for t1 in schedule[k]["time"]]
                            schedule[k]["aquired"]=[time_now.time() > t_schedule.time()
                                                    for t_schedule in schedule_time]
                        #se guarda el dia actual
                        schedule[key]["actual_day"] = time_now.strftime("%Y-%m-%d")

                else:
                    shcedule_times = [datetime.datetime.strptime(
                        t1, "%H:%M:%S") for t1 in schedule[key]["time"]]
                    
                    #si ya ha pasado el tiempo y aquire es falso
                    for i, t in enumerate(shcedule_times):
                        if (time_now.time() > t.time() 
                                and not schedule[key]["aquired"][i]):

                            #se envia una señal al loop pricipal
                            queue.put(schedule[key]["command"])
                            schedule[key]["aquired"][i] = True

            # print(time_now)
            sleep(1)