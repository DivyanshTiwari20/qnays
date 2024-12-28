import sys

class customexception(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message
        _, _, exc_tb = error_detail.exc_info()
        self.line_number = exc_tb.tb_lineno
        
    def __str__(self):
        return f"Error occurred in python script name [{exc_tb.tb_frame.f_code.co_filename}] line number [{exc_tb.tb_lineno}] error message [{str(self.error_message)}]"