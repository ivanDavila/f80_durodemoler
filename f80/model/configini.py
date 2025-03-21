import json

def read_config(config_file : str) -> dict:
    try:
        data_dir = {}
        with open(config_file, 'r') as config:
            data_info = config.read()
            data_dir = json.loads(data_info)
            # print(data_dir)
            print("Loding config.ini successfully")
        return data_dir['configuracion']

    except Exception as e:
        print("Error: %s" % e)
        return {}

def write_config(config_file, configlist):
    with open(config_file, 'w+') as config:
        data_dir = {'configuracion':[]}
        data_dir['configuracion'] = configlist
        data_info = json.dumps(data_dir, indent=2)
        config.write(data_info)