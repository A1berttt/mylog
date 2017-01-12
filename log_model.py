import logging
import os

class TheLogger:
    def __init__(self, user):
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.INFO)

        self.logName = "log.log"
        self.isExist = os.path.exists(self.logName)
        if self.isExist:
            os.remove(self.logName)

        self.fh = logging.FileHandler("log.log")
        self.fh.setLevel(logging.INFO)
        self.formartter = logging.Formatter('ClassName:%(asctime)s - %(name)s  - %(message)s')
        self.fh.setFormatter(self.formartter)
        self.logger.addHandler(self.fh)
        self.logger.info("dddd")