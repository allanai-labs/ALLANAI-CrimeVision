# src/fetch_crime_data.py

import requests
import pandas as pd
import os
from datetime import datetime

def fetch_crime_for_month(lat, lng, month_str):
    """
    Fetch crime data for a location (latitude, longitude) for the given month (yyyy-mm).
    Returns a DataFrame.
    """
    url = "https://data.police.uk/api/crimes-street/all-crime"
    params = {
        "lat": lat,
        "lng": lng,
        "date": month_str
    }
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print("Error:", resp.status_code, resp.text)
        return pd.DataFrame()
    data = resp.json()
    return pd.DataFrame(data)

def fetch_and_save(month_str, lat, lng, save_path):
    df = fetch_crime_for_month(lat, lng, month_str)
    if df.empty:
        print("No data fetched for", month_str)
        return
    # Save to CSV
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print("Saved:", save_path, "with", len(df), "rows")

if __name__ == "__main__":
    # example: London approximate center
    london_lat = 51.5074
    london_lng = -0.1278
    month = "2023-01"
    output_file = "data/raw/london_crime_2023-01.csv"
    fetch_and_save(month, london_lat, london_lng, output_file)
