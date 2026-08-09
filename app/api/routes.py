from fastapi import APIRouter
from app.models.schemas import PredictionResponse , PredictionRequest
from app.services.predictor import predict_air_quality 

router = APIRouter() 

@router.get("/")
async def home ()  : 
    return {
        "message"  : "Air  Quality Prediction API" , 
        "version"  : "1.0.0"
    }
@ router.get("/health")
async def health() : 
    return {
        "status" :"healthy"  , 
        "model" : "loaded"
    }    
@router.post(
    "/api/v1/predict" , 
    response_model= PredictionResponse
)
async def predict( data : PredictionRequest) :
    return predict_air_quality( data)
