import os
import pathlib


ROOT_FOLDER = pathlib.Path(__file__).resolve().parent

STATIC_URL = 'static'

STATIC_FOLDER = os.path.join(ROOT_FOLDER, STATIC_URL)
