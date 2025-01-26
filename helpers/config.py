import configparser

class Config(object):

    def getLink(self, type) :
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['SERVER_LINKS'][type]

    def getSection(self, section) :
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config[section]