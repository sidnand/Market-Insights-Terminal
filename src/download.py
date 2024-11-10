from typing import List, Tuple, Dict, Literal

import pandas as pd

import ipdb
import tqdm

import edgar
import yfinance as yf

from src.util import *

edgar.set_identity(f"{CONFIG['user']['name']} <{CONFIG['user']['email']}>")

USA_TICKERS = get_tickers(HEADERS)

def download_economy(id: str) -> pd.DataFrame:
    """Downloads data from the Federal Reserve Economic Data (FRED) API."""

    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={id}&api_key={CONFIG['api_key']['fred']}&file_type=json"
    print(f"Downloading data from {url}...")
    
    data = download(url, HEADERS)
    if not data:
        print("No data found.")
        return None

    data_json = data.json()
    data_series = data_json.get("observations", [])
    data_csv = pd.DataFrame(data_series)[['date', 'value']].set_index('date')
    data_csv.index = pd.to_datetime(data_csv.index)
    data_csv = data_csv.sort_index()
    return data_csv

def process_filing(filing: edgar.Filing) -> dict:
    """Extracts balance sheet, income statement, and cash flow statement from a filing."""

    statements = {}
    for statement_type in ["balance_sheet", "income_statement", "cash_flow_statement"]:
        func_name = f"get_{statement_type}"
        if hasattr(filing.obj().financials, func_name):
            statement_df = getattr(filing.obj().financials, func_name)().get_dataframe()
            if statement_df is not None:
                statement_df = statement_df.set_index("concept")
                statements[statement_type] = statement_df
        else:
            print(f"Warning: '{func_name}' not available in filing.")
    return statements

def get_filings_data(filings: list, description: str) -> dict:
    """Processes filings and returns a dictionary of concatenated statements by type."""

    statements_data = {"balance_sheet": [], "income_statement": [], "cash_flow_statement": []}
    
    for filing in tqdm.tqdm(filings, desc=f"Processing {description} filings"):
        processed_statements = process_filing(filing)
        for statement_type, statement_df in processed_statements.items():
            statements_data[statement_type].append(statement_df)

    for statement_type, data_list in statements_data.items():
        if data_list:
            concatenated_df = pd.concat(data_list, axis=1).iloc[:, ::-1]
            concatenated_df = concatenated_df[~concatenated_df.index.duplicated(keep='last')]
            statements_data[statement_type] = concatenated_df
    
    return statements_data

def download_ticker(
    ticker: str, 
    type: Literal["annual", "quarterly"],  # only "annual" or "quarterly"
    n: int = 3
) -> pd.DataFrame:
    """Downloads and processes financial data for a given ticker."""

    company = edgar.Company(ticker)
    print(f"Downloading data for {ticker}...")

    form = "10-K" if type == "annual" else "10-Q"
    n = n if type == "annual" else 4 * n
    
    filings = company.get_filings(form=form).latest(n)

    print(f"Finished downloading data for {ticker}.")

    report = get_filings_data(filings, type)

    # remove columns with duplicated names
    for key in report:
        report[key] = report[key].loc[:, ~report[key].columns.duplicated()]

    print("Finished processing all data.")
    return report

def download_stock(ticker: str) -> pd.DataFrame:
    """Downloads stock price data from Yahoo Finance."""

    data_daily = yf.download(ticker, period="max", interval="1d")
    data_daily = data_daily.droplevel(1, axis=1)

    return data_daily


