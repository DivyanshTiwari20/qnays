# import sys

# class customexception(Exception):
#     def __init__(self, error_message, error_detail):
#         self.error_message = error_message
#         _, _, self.exc_tb = error_detail.exc_info()
#         super().__init__(self.error_message)
    
#     def __str__(self):
#         return f"Error: {self.error_message} [line {self.exc_tb.tb_lineno}]"

class customexception(Exception):
    def __init__(self, message, sys_module):
        super().__init__(message)
        self.sys_info = sys_module.exc_info()
