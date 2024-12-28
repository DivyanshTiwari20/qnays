class customexception(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_detail = error_detail
        _, _, self.exc_tb = error_detail.exc_info()
        
    def __str__(self):
        return f"Error occurred in python script name [{self.exc_tb.tb_frame.f_code.co_filename}] line number [{self.exc_tb.tb_lineno}] error message [{str(self.error_message)}]"