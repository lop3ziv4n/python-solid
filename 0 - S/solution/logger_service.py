class LoggerService:

    def info(self, info):
        # code into information in log file
        f = open("infoLog.txt", "a")
        f.write(info)
        f.close()

    def debug(self, debug):
        # code into debug in log file
        f = open("debugLog.txt", "a")
        f.write(debug)
        f.close()

    def error(self, error):
        # code into error in log file
        f = open("errorLog.txt", "a")
        f.write(error)
        f.close()
