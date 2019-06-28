#!/bin/python3

# QuickLog - A simple Logger with different methods of use
#
# HAX   - Version 1.0

import logging


class QuickLog:

    def __init__(self, logfile, hostname, application):
        self.host = hostname
        self.app = application
        self.file = logfile
        # lookup levels in wiki if not sure
        self.levels = {0:"debug", 1:"info", 2:"warn", 3:"error", 4:"crit"}
        # Setup Logging instance for further use
        self.logger = logging.getLogger(self.app)
        self.logger.setLevel(logging.DEBUG)
        # Add File Handler
        logger_fh = logging.FileHandler(self.file)
        logger_fh.setLevel(logging.DEBUG)
        # Add Console Handler
        logger_ch = logging.StreamHandler()
        logger_ch.setLevel(logging.ERROR)
        # Add Format
        formatter = logging.Formatter('%(asctime)s - %(name)-16s - %(levelname)-8s - %(message)s')
        logger_fh.setFormatter(formatter)
        logger_ch.setFormatter(formatter)
        # Add Handlers to logger
        self.logger.addHandler(logger_fh)
        self.logger.addHandler(logger_ch)


    def getlevels(self):
        return self.levels


    def log(self, level, message):
         if level == 4:
             self.logger.critical(message)
         elif level == 3:
             self.logger.error(message)
         elif level == 2:
             self.logger.warning(message)
         elif level == 1:
             self.logger.info(message)
         elif level == 0:
             self.logger.debug(message)
         else:
             self.logger.error('Unknown level, logged message: ' + message)


    def export(self, destination):
        with open(self.file) as input:
            content = input.readlines()
            with open(destination, 'w') as output:
                for line in content:
                    output.write(line)


    def help(self):
        helptext = """
        ###########################
        # QuickLog Logging Module #
        #############################################################
        #
        #   Log-Levels:
        #   ------------------------------------------------------
        #
        #   %s
        #
        #   ______________________________________________________
        #
        #   Usage:
        #   ------------------------------------------------------
        #
        #       from quicklog import QuickLog
        #
        #       ...
        #       x = QuickLog(logfile, hostname, application)
        #       x.log(0, "This message is level DEBUG")
        #       x.getlevels()       # Shows all known levels
        #       x.help()            # Prints this manual
        #       ...
        #
        #
        #############################################################
        """
        return print(helptext % (self.levels))
