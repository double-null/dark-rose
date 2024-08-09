from datetime import datetime

class Monolog:

    def log(self, filename, text):
        filepath = filename + '.log'
        period = datetime.today().strftime('[%d.%m.%Y %H:%M]')
        line = period + ' ' + text + "\n"
        file = open(filepath, "a+")
        file.write(line)
        file.close()