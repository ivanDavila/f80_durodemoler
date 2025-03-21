import json
# from f80 import errorManager

def read_config(config_file):
    data_dir = {}
    with open(config_file, 'r') as config:
        data_info = config.read()
        data_dir = json.loads(data_info)
        # print(data_dir)
        print("Loding config.ini successfully")
    return data_dir

def write_config(config_file, config_dictionary):
    with open(config_file, 'w+') as config:
        data_dir = {'configuracion':[]}
        data_dir = config_dictionary
        data_info = json.dumps(data_dir, indent=2)
        config.write(data_info)
