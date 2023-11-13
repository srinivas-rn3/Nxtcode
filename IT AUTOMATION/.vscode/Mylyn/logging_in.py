import logging
'''
name = 'GEG'
logging.error('%s raised as error',name)
'''
'''
file_name = r"C://Users//srini//OneDrive//Documents//python_test.log"
logging.basicConfig(filename=file_name,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.debug("Harmless debug message")
logging.info("Just information")
logging.warning("Its warning")
logging.error("Did you try to divide by zero")
logging.critical("Fuck you app in down")
'''

import logging.config 
'''
#logging.config.fileConfig(r'C:\Users\srini\OneDrive\Documents\/temp.conf.txt')
logger = logging.getLogger('simpleExample')
logger.debug("Debug message")
logger.info("info message")
logger.warning("Just warning")
logger.error("Error message")
logger.critical("Fuck you App is down")
'''


logging.basicConfig(format =' %(levelname)s - %(message)s')
logging.warning("This is the message")

name = "fuck"
logging.error(f'{name} raised error')