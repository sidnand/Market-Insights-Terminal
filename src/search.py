import pandas as pd

from src.util import *

USA_TICKERS = get_tickers(HEADERS)

def search_ticker(query: str) -> None:
    query = query.lower()

    data = USA_TICKERS[USA_TICKERS["title"].str.contains(query, case=False, na=False) | USA_TICKERS["ticker"].str.contains(query, case=False, na=False)]
    data = data.drop_duplicates().set_index("cik_str")

    with pd.option_context('display.max_colwidth', 120, 'display.max_rows', None):
        print(data)

def search_economy(query: str) -> None:
    query = query.lower()
    query = query.replace(" ", "+")

    url = f"https://api.stlouisfed.org/fred/series/search?search_text={query}&api_key={CONFIG["api_key"]["fred"]}&file_type=json"

    data = download(url, HEADERS)
    if not data: print("No data found.")

    data_json = data.json()

    data_series = data_json.get("seriess", [])
    data_csv = pd.DataFrame(data_series)[['id', 'popularity', 'notes']].dropna().set_index('id')
    data_csv = data_csv[data_csv['popularity'] > 10]
    data_csv = data_csv.sort_values(by='popularity', ascending=True)

    data_csv['notes'] = data_csv['notes'].apply(lambda x: x.split("\n")[0])

    for index, row in data_csv.iterrows():
        print(f"ID: {index}")
        print(f"Popularity: {row['popularity']}")
        print(f"Notes: {row['notes']}")
        print()

