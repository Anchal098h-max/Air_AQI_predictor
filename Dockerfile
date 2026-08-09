## base python Image 
FROM python:3.14-slim
## working directory 
WORKDIR /app
# cpy requirement .txt
COPY requirements.txt .
## install python packages 
RUN pip install --no-cache-dir -r requirements.txt
### copy 
COPY  . .
# Expore fastapi port 
EXPOSE 8000

## start fastapi 
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]