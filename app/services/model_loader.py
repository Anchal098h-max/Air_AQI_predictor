from pathlib import Path
from app.config import MODEL_PATH , PREPROCESSOR_PATH
import joblib

model  = None 
preprocessor = None

def load_artifacts():
    global model , preprocessor 
    
    if model is None : 
         model = joblib.load(MODEL_PATH)
    
    if preprocessor is None :      
         preprocessor = joblib.load(PREPROCESSOR_PATH)

    return model, preprocessor
