from fastapi import FastAPI , Request
from app.core.middleware import LoggingMiddleware
from app.api.routes import router 
from fastapi.responses import JSONResponse
from app.core.exceptions import PredictionException 
app = FastAPI (
    title= "Air Quality Prediction API" , 
    description = "Production-ready Air Quality  Predictor API using FastAPi" , 
    version= "1.0.0" , 
    docs_url= "/docs" , 
    redoc_url= "/redoc" 
)
app.add_middleware( LoggingMiddleware)
app.include_router(router)

@app.exception_handler(PredictionException)
async def  prediction_exception_handler(
    request : Request  , 
    exc : PredictionException
):
    return JSONResponse(
        status_code= exc.status_code, 
        content= {
            "status" : "error", 
            "message" : exc.detail
        }
    )
    