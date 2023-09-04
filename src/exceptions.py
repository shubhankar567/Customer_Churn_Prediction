import sys, os
from src.logger import logging

def get_error_details(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    message = f'Error occured in {filename} at line number [{line_no}]. The error: {error}'
    return message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_details(error = error_message, error_details = error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == '__main__':
    try:
        logging.info('Exception File initiated')
        a = 1/0
    except Exception as e:
        logging.info('Division by Zero Error')
        raise CustomException(e, sys)
