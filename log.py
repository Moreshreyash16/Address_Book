import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
handlers=[
        logging.StreamHandler(),  # Stream logs to the console
        logging.FileHandler('address,log')  # Store logs in a file
    ])

    # Create a logger
logger = logging.getLogger('my_logger')