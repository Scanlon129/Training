import logging, os

#Logging----------------------------------------------------------------------
'''
Going forward: create logging configs, set configs, split into separate
module or class to be called
'''
# Define logger and path
logger = logging.getLogger(name=__name__)
logger.setLevel(logging.debug)
log_path = 'C:\\Users\\scanl\\OneDrive - BUTLER-TILL MEDIA SERVICES\\\
        =Coding\\Python\\Logs'
# Set overall logging format
formatter = logging.formatter('%(asctime)s: %(message)s')
# Set file logging filename, level and format
log_file_handler = logging.FileHandler(log_path + 'debug.log')
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)
#Set error file logging filename, level and format
error_log_file_handler = logging.FileHandler(log_path + 'errors.log')
error_log_file_handler.setLevel(logging.ERROR)
error_log_file_handler.setFormatter(formatter)
logger.addHandler(error_log_file_handler)
#Set console logging level and format
log_stream_handler = logging.StreamHandler()
log_stream_handler.setFormatter(formatter)
logger.addHandler(log_stream_handler)

logging.debug(f'The file {os.path.basename(__file__)} was logged')
