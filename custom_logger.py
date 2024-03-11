import logging

class CustomLogger:
    def __init__(self, log_file='app.log'):
        # Configura el logger
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def log_info(self, message):
        print(message)
        logging.info(message)

    def log_warning(self, message):
        print(message)
        logging.warning(message)

    def log_error(self, message):
        print(message)
        logging.error(message)
