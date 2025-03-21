from os.path import abspath, dirname
import sys
import traceback
from datetime import datetime

appDir = abspath(dirname(sys.argv[0]))

def errorManager(error):
    traceback.print_tb(error.__traceback__)
    print("Error: %s" % error)
    currentDT = datetime.now()
    errorfile_name = appDir + "/" + "error-log.txt"
    errorfile = "%s" % (errorfile_name)
    # parent.log("Error: %s" % error)
    with open(errorfile, "a") as f:
        f.write("\n [%.2d%.2d%.2d-%.2d%.2d%.2d]Error: %s" % (
            currentDT.year, 
            currentDT.month, 
            currentDT.day, 
            currentDT.hour, 
            currentDT.minute, 
            currentDT.second, 
            error
            )
        )


if __name__ == "__main__":
    try:
        data = 1/0

    except Exception as e:
        errorManager(e)