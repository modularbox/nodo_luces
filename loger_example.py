from custom_logger import CustomLogger

def main():
    # Crear una instancia del logger
    logger = CustomLogger()

    # Log algunos mensajes de prueba
    logger.log_info('Este es un mensaje de información.')
    logger.log_warning('¡Cuidado! Esto es una advertencia.')
    logger.log_error('¡Error! Algo salió mal.')

if __name__ == "__main__":
    main()
