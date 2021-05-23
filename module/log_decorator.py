import logging
import functools
path = r"log/new_log.txt"

def _generate_log():
    
    
    # Create a logger and set the level.
    logger = logging.getLogger('LogError') # create a logger object
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        # Create file handler
        file_handler = logging.FileHandler(path) # path: Path of the log file.

        # for log format attributes.
        formatter = logging.Formatter('[%(levelname)s] : [%(funcName)s] : %(message)s')
        #add the format to file handler
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)

        logger.addHandler(file_handler)
    
    return logger


def log_error(path='<path>/log.error.log'):
    """
    We create a parent function to take arguments
    :param path:
    :return:
    """

    def error_log(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            try:
                # Execute the called function, in this case `divide()`.
                # If it throws an error `Exception` will be called.
                # Otherwise it will be execute successfully.
                return func(*args, **kwargs)
            except Exception as e:
                logger = _generate_log(path)
                error_msg = 'And error has occurred at /' + func.__name__ + '\n'
                logger.exception(error_msg)

                return e  # Or whatever message you want.

        return wrapper

    return error_log
