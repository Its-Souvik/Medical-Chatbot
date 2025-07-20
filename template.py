import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')

list_of_files = [
        "src/__init__.py",
    "src/helpers.py",
    "src/prompt.py",
    "env",
    "setup.py",
    "app.py",
    "research/trails.ipynb"
   
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")
    else:
        logging.info(f"File {filename} is in the root directory.")

    # ✅ Create empty file if not exists
    if not filepath.exists():
        with open(filepath, "w") as f:
            f.write(f"# This is {filename}\n")
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
