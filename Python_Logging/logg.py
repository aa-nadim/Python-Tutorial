from logging import*
LOG_FORMAT = '[{asctime} {name}] {message} {lineno}'
basicConfig(filename='logfile.log',level=DEBUG, filemode='w', style='{', 
 format=LOG_FORMAT)

logger = getLogger('Asia/Dhaka')
logger.debug("This is Debug")
logger.info("This is Warning")
logger.warning("This is Warning")
logger.error("This is Error")
logger.critical("This is Critical")