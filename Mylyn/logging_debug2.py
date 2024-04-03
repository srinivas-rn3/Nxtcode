import logging 
#name = 'Fuck'
#logging.error(f'{name} is the error with name')
'''
a = 9 ;b = 0
try:
    c = a/b 
except:
    logging.error("Exception occured",exc_info=True)
'''
file_name = r"C://Users//srini//OneDrive//Documents//python_test1.log"
a = 9
b = 0
logging.basicConfig(filename=file_name)
try:
    c = a/b 
except:
    logging.exception("Exception occured!!!")