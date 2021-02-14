import logging
#Create and configure logger
LOG_FORMAT = "%(Levelname)s %(asctimr)s - %(message)s"
logging.basicConfig(filename = "D:\Programming\Python\pythonCode\Lumberjack.Log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode='w')
logger=logging.getLogger()

#Test the logger

logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")