from datetime import datetime
from utils import constants

# Log request errors to a file
def log_to_file(message):
    now = datetime.now().strftime("%H:%M:%S")
    log = f"[{now}]: {message}"
    
    # Append log to the file, create file if file doesn't exist
    try:
        with open(constants.logger, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        content = ''

    updated_content = log + '\n' + content

    try:
        with open(constants.logger, 'w') as file:
            file.write(updated_content)
    except:
        print("Something went wrong while trying to log.")
