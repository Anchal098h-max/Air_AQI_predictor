# 🌍 Air Quality Prediction API

A production-ready Machine Learning API built using **FastAPI**, **LightGBM**, **Scikit-Learn**, **Docker**, and **Docker Compose**.

The API predicts the **Air Quality Index (AQI)** from atmospheric pollutant concentrations and returns both the predicted AQI value and its corresponding AQI category.

---

# 🚀 Features

- ⚡ FastAPI REST API
- 🤖 LightGBM Regression Model
- 🧠 Feature Engineering Pipeline
- 📊 Data Preprocessing Pipeline
- ✅ Input Validation using Pydantic
- 📁 Clean Project Architecture
- 📝 Centralized Logging
- ⚠️ Custom Exception Handling
- 🔄 Middleware Support
- 🐳 Dockerized Application
- 🐳 Docker Compose Support
- 🧪 API Testing
- 📦 Production Ready

---

# 📂 Project Structure

```text
AirQuality/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── config.py
│   │
│   ├── core/
│   │   ├── logger.py
│   │   ├── middleware.py
│   │   ├── exceptions.py
│   │   └── helper.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── services/
│   │   ├── model_loader.py
│   │   └── predictor.py
│   │
│   ├── utils/
│   │   └── category.py
│   │
│   ├── feature_engineering.py
│   └── main.py
│
├── models/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── tests/
│   └── test_api.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
└── README.md
```

---

# 🧠 Machine Learning Pipeline

### Models Evaluated

- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- **LightGBM Regressor (Selected)**

### Final Model

The deployed model is:

**LightGBM Regressor**

It was selected after comparing multiple machine learning algorithms based on predictive performance.

---

# ⚙️ Feature Engineering

The prediction pipeline automatically creates engineered features before sending data to the model.

Generated Features

- Pollution Load
- Gas Total
- VOC
- Particle Features
- NO₂ / SO₂ Ratio
- Other engineered environmental features

---

# 📊 Input Features

| Feature |
|----------|
| PM2.5 |
| PM10 |
| NO |
| NO2 |
| NOx |
| NH3 |
| CO |
| SO2 |
| O3 |
| Benzene |
| Toluene |
| Xylene |

---

# 📌 AQI Categories

| AQI | Category |
|------|----------|
| 0 – 50 | Good |
| 51 – 100 | Satisfactory |
| 101 – 200 | Moderate |
| 201 – 300 | Poor |
| 301 – 400 | Very Poor |
| > 400 | Severe |

---

# 🛠 Tech Stack

## Backend

- FastAPI
- Uvicorn
- Pydantic

## Machine Learning

- LightGBM
- Scikit-Learn
- Pandas
- NumPy

## Deployment

- Docker
- Docker Compose

## Utilities

- Logging Middleware
- Exception Handling
- Feature Engineering
---

# 📦 Installation

Clone the repository

```bash
git clone <repository-url>
```

Move inside the project

```bash
cd AirQuality
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open

```
http://localhost:8000/docs
```

---

# 🐳 Docker

## Build Image

```bash
docker build -t air-quality-api .
```

## Run Container

```bash
docker run -p 8000:8000 air-quality-api
```

---

# 🐳 Docker Compose

Build & Run

```bash
docker compose up --build
```

Stop

```bash
docker compose down
```

---

# 📡 API Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 📤 Prediction Endpoint

## POST
So now there are two processes.


```
/api/v1/predict
```

### Sample Request

```json
{
    "PM2_5":45,
    "PM10":90,
    "NO":12,
    "NO2":20,
    "NOx":30,
    "NH3":15,
    "CO":0.8,
    "SO2":10,
    "O3":25,
    "Benzene":1.2,
    "Toluene":2.1,
    "Xylene":0.5
}
```

### Sample Response

```json
{
    "predicted_aqi": 134.72,
    "category": "Moderate"
}
```

---

# 🧪 Testing

Run all tests

```bash
pytest
```

---

# 📈 Logging

Every prediction request is logged.

Example

```
Prediction Started

Prediction Completed

AQI = 134.72

Category = Moderate
```

---

# ⚠️ Exception Handling

The API provides centralized exception handling for

- Invalid Inputs
- Prediction Errors
- Model Errors
- Internal Server Errors

---

# 🔒 Validation

Request validation is performed using **Pydantic**.

All pollutant values are validated before prediction.

---

# 📄 Future Improvements

- Authentication
- Rate Limiting
- Health Check Endpoint
- Model Information Endpoint
- CI/CD Pipeline
- Cloud Deployment (Render / AWS / Azure)
- Monitoring & Metrics

---

# 👨‍💻 Author

**Anchal kumar **

Machine Learning | FastAPI | Backend Development | Docker | Data Science

---

# 📜 License

This project is developed for educational and portfolio purposes.