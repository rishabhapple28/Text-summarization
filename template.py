import os
from pathlib import Path


import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s:')

project_name = "Text-SUmmarizer"

file_list = [

".github/workflows/.gitkeep",
f"src/{project_name}/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/utils/__init__.py",
f"src/{project_name}/utils/common.py",
f"src/{project_name}/logging/__init__.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/__init__.py",
f"src/{project_name}/entity/__init__.py",
f"src/{project_name}/constant/__init__.py",

"config/config.yaml",
"parameter.yaml",
"app.yaml",
"main.py",
"dockerfile",
"requirements.txt",
"setup.py",
"research/trials/trials.ipynb",



]



for filepath in file_list:
    filepath =Path(filepath)
    file_directory, file_name = os.path.split(filepath)

    if file_directory != "":
        os.makedirs(file_directory,exist_ok=True)
        logging.info(f"Directory {file_directory} created")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"New File {filepath} created")
    
    else:
        logging.info(f"File {filepath} already exists")

