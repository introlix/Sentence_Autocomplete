import sys
from autoLix.logger import logging
from autoLix.exception import CustomException

logging.info("Lets do it")
def divide_two_number(a, b):
    try:
        return a/b
    except Exception as e:
        raise CustomException(e, sys) from e
    
print(divide_two_number(10, 0))