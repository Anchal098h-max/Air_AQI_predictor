import pandas as pd 
from app.models.schemas import PredictionRequest , PredictionResponse
from app.services.model_loader import load_artifacts
from app.utils.category import get_aqi_category
from app.config import EXPECTED_COLUMNS

from app.feature_engineering import create_features
from app.core.logger import logger 
from app.core.exceptions import PredictionException


def predict_air_quality (data:PredictionRequest) -> PredictionResponse: 
 try : 
        model, preprocessor = load_artifacts()
        logger.info( "Prediction Started")
        df = pd.DataFrame([data.model_dump()]) # conveet the reqest into data frame 
        df.rename(columns={"PM2_5": "PM2.5"}, inplace=True)
        df = create_features(df)
        expected_columns  = EXPECTED_COLUMNS
        for column in expected_columns:
           if column not in df.columns:
               df[column] = None

  
        if expected_columns:
           df = df[expected_columns]
        else:
           df = df.drop(["AQI", "AQI_Bucket"], axis=1, errors="ignore")

        transformed = preprocessor.transform( df)
        prediction  = model.predict(transformed)[0] ## predict AQI 
        category = get_aqi_category(prediction) ## aqi categoty 
        logger.info(f"Prediction Completed | AQI ={prediction  : .2f} | Category = { category}"
        )
        return PredictionResponse(
        predicted_aqi= round(float(prediction) , 2) , 
        category= category
       )
 except Exception as e : 
     logger.exception( "Prediction Failed")
     raise PredictionException(
        detail=f" Prediction Failed:{str(e)}"
     )
           
    
