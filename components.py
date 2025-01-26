import configparser

def load_config() :
    config = configparser.ConfigParser()
    config.read('config.ini')
    return {
        'dk_start': config['SERVER_LINKS']['dk_start'],
        'dk_server': config['SERVER_LINKS']['dk_server'],
        'speed': config['MAIN']['speed_click'],
        'speed_load': int(config['MAIN']['speed_load']),
        'actions': config['ACTIONS'],
    }