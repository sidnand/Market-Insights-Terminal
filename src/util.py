import os
import requests
import json

import pandas as pd

CONFIG_FILE = "config.json"

DATA_DIR = "data/"
FRED_DIR = "data/fred/"
TICKER_DIR = "data/ticker/"

USA_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"

USA_TICKERS = None

if not os.path.exists(FRED_DIR):
    os.makedirs(FRED_DIR)

if not os.path.exists(TICKER_DIR):
    os.makedirs(TICKER_DIR)

with open(CONFIG_FILE, "r") as f:
    CONFIG = json.load(f)

HEADERS = {
    "User-Agent": f"{CONFIG['user']['name']} <{CONFIG['user']['email']}>"
}

def export(data: pd.DataFrame, path: str) -> None:
    parent_dir = os.path.dirname(path)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    if path.endswith(".csv"):
        data.to_csv(path)
    elif path.endswith(".xlsx"):
        data.to_excel(path)
    else:
        print("Invalid file format. Please provide a .csv or .xlsx file.")

def download(url: str, header: dict) -> requests.Response:
    r = requests.get(url, headers=header)
    if r.status_code != 200:
        print(f"Failed to download data from {url}.")
        print(f"Status code: {r.status_code}")
        print(f"Reason: {r.reason}")
        return None
    
    return r

def get_tickers(header: dict) -> pd.DataFrame:
    global USA_TICKERS

    if USA_TICKERS is not None:
        return USA_TICKERS

    data = download(USA_TICKERS_URL, header)
    data_json = data.json()
    data_df = pd.DataFrame(data_json)
    data_df = data_df.T

    USA_TICKERS = data_df
    
    return data_df