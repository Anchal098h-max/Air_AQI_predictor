from typing import Any
import pandas as pd 
from app.config import EXPECTED_COLUMNS

def rename_columns( df : pd.DataFrame)  -> pd.DataFrame:
     ''' Rename API input cols to match trainnig cols  ''' 
     df = df.copy()
     df.rename (
         columns= {
             "PM2_5":"PM2.5"
         } , inplace= True 
     )
     return df 
 ## columns align 
def safe_round( value : Any , digits : int = 2) -> float : 
    """ round it """     
    return round(float(value) , digits)
