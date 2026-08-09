from pydantic import BaseModel , Field
class PredictionRequest( BaseModel) :
    PM2_5 : float = Field(..., ge =0 ,  description= "PM2.5 concentration")
    PM10 : float = Field( ...  , ge =0 ) 
    NO : float  = Field ( ... , ge =0 )
    NO2 : float  = Field( ..., ge =0 )
    NOx : float   = Field( ... , ge =0)
    NH3 : float  = Field( ... , ge= 0)
    CO  : float = Field( ... , ge =0 )
    SO2 : float  = Field( ... , ge =0 )
    O3 :  float = Field( ... , ge= 0)
    Benzene : float  = Field( ..., ge =0 )
    Toluene : float  = Field ( ... , ge =0 )
    Xylene : float = Field( ... , ge =0 )
class PredictionResponse( BaseModel):
    predicted_aqi : float
    category : str         
    