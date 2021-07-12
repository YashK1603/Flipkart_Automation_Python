import inspect
import logging


def customLogger(logLevel=logging.DEBUG):

    # stack() will assign the loggername according to the class name
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # setting log level as DEBUG so all type of log will be displayed
    logger.setLevel(logging.DEBUG)

    # Defining static file name and appending log results with every tests run
    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    # Formatting the log sentence
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
