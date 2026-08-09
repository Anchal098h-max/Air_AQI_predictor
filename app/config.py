from pathlib import Path 
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "artifacts" / "model.pkl"
PREPROCESSOR_PATH = BASE_DIR/ "artifacts"/"preprocessor.pkl"
EXPECTED_COLUMNS = [
    "PM2.5",
    "PM10",
    "NO",
    "NO2",
    "NOx",
    "NH3",
    "CO",
    "SO2",
    "O3",
    "Benzene",
    "Toluene",
    "Xylene",
    "AQI_Bucket",
    "No-grp",
    "Particales",
    "NO2_SO2",
    "VOC",
    "Pollution_Load",
    "Gas_Total",
]
