# Download Manager for csv 
# Move csv files from default downloads folder to csvfolder

import os
import shutil
from dotenv import load_dotenv

load_dotenv()
PATH = os.environ.get("DEFAULTDOWNLOADS")
CSVPATH = os.environ.get("CSVFOLDER")
try:
    with os.scandir(PATH) as files:
        for file in files:
            if ".csv" in file.name:
                shutil.move(file, CSVPATH)
        print("csv files moved to csvfolder")
except:
    print("Failed to move csv files")