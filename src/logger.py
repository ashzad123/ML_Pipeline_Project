# Original logger using logging module of python

# import logging
# import os
# from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
# logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# # Example usage
# # if __name__ == "__main__":
# #     logging.info("Logging setup complete.")


# Revised logger using loguru
from loguru import logger
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# Create log file inside the timestamped folder
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logger.add(LOG_FILE_PATH, format="{time} {file.name} {line} {level} {message}", level="INFO")

# Example usage
# if __name__ == "__main__":
#     logger.info("Logging setup complete.")