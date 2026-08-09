import time   ## this is the security guard at the enterance of API 
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware  # this  tell i am creating  my own middleware 
from app.core.logger import logger

class LoggingMiddleware(BaseHTTPMiddleware):
    async def  dispatch( self , request : Request , call_next): ## the functions runs for every request 
        start_time = time.perf_counter() 
        response  = await call_next( request) ## this sends the request to your your route 
        process_time  = time.perf_counter() - start_time 
        logger.info(
            f"{request.method}| "
            f"{request.url.path}| "
            f"Sataus = {response.status_code} |"
            f"Time = {process_time:.4f}sec"
        )
        return response
    