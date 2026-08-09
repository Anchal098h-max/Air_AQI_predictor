def create_features(df):
    
    df["No-grp"] = df["NH3"] * df["NOx"]

    df["Particales"] = df["PM2.5"] * df["PM10"]

    df["NO2_SO2"] = df["NO2"] + df["SO2"]

    df["VOC"] = (
        df["Benzene"]
        + df["Toluene"]
        + df["Xylene"]
    )

    df["Pollution_Load"] = (
        df["PM2.5"]
        + df["PM10"]
        + df["NOx"]
    )

    df["Gas_Total"] = (
        df["NO"]
        + df["NO2"]
        + df["NOx"]
        + df["SO2"]
        + df["CO"]
    )

    return df
