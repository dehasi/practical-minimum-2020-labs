import logging
import logging.config



# logging.config.fileConfig('logging.conf')

logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
logging.info('This param1: %s  param2: %s', 1, 2)


#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.warning('This will get logged to a file')
