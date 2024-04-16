import logging 
'''
# Configure logging

logging.basicConfig(
    filename = file,
    format = '%(asctime)s -- %(levelname)s -- %(message)s',
    level = logging.DEBUG
)

#log message
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")

#create a named logger
logger = logging.getLogger('example_log')
logger.info("This is a message from a named logger")

#exception logging
try:
    result = 1 / 0
except ZeroDivisionError as e:
    logging.error('An error occurred: %s',e,exc_info=True)
'''
'''

To display log messages both in the console and in a file simultaneously, 
you can use multiple handlers in Python's logging module. Here's 
how you can modify your code to achieve this:
'''
file = r"C:\Users\srini\OneDrive\Documents\app_4.log"
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s --- %(levelname)s --- %(message)s',
    handlers=[
        logging.FileHandler(filename=file),
        logging.StreamHandler()
    ]
)
try:
    result = 1 / 0 
except Exception as e:
    logging.error("An error occured : %s",e)