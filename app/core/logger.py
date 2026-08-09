import logging
from pathlib import Path  ## used to create the folders 
LOG_DIR = Path("logs") ## create new folder 
LOG_DIR.mkdir( exist_ok= True) # create folder if does not exixts
# configure logging 
logging.basicConfig (
    level= logging.INFO , 
    format= "%(asctime)s | %(levelname)s | %(message)s" ,  ## controls  how log looks 
    handlers= [
        logging.FileHandler(LOG_DIR/"app.log") , 
        logging.StreamHandler()
    ]
) 
logger = logging.getLogger("air_quality_api")

