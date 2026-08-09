import anyio
import httpx
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app.main import app

sample_data = {
    "PM2_5": 45.0,
    "PM10": 90.0,
    "NO": 12.0,
    "NO2": 20.0,
    "NOx": 30.0,
    "NH3": 15.0,
    "CO": 0.8,
    "SO2": 10.0,
    "O3": 25.0,
    "Benzene": 1.2,
    "Toluene": 2.1,
    "Xylene": 0.5
}

async def send_predict_request():
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:
        return await client.post(
            "/api/v1/predict",
            json=sample_data
        )


def test_predict_endpoint():
    response = anyio.run(send_predict_request)

    assert response.status_code == 200

    assert response.headers["content-type"].startswith("application/json")

    data = response.json()

    assert "predicted_aqi" in data
    assert "category" in data

    assert isinstance(data["predicted_aqi"], (float, int))
    assert isinstance(data["category"], str)


if __name__ == "__main__":
    response = anyio.run(send_predict_request)
    print("Status code:", response.status_code)
    print("Response:", response.json())
