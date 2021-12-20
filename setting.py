import os
import pathlib

# Server settings
SERVER_HOST = 'localhost'

SERVER_PORT = 5000


# Static files folder settings
ROOT_FOLDER = pathlib.Path(__file__).resolve().parent

STATIC_URL = 'static/'

STATIC_FOLDER = os.path.join(ROOT_FOLDER, STATIC_URL)
