from src.util import *
from src.ratios import *

def compute_ratios(ticker: str) -> None:
    annual_bs_path = f"{TICKER_DIR}{ticker}/annual_balance_sheet.csv"
    annual_is_path = f"{TICKER_DIR}{ticker}/annual_income_statement.csv"
    annual_cf_path = f"{TICKER_DIR}{ticker}/annual_cash_flow_statement.csv"

    if not os.path.exists(annual_bs_path) or not os.path.exists(annual_is_path) or not os.path.exists(annual_cf_path):
        print(f"Annual data for {ticker} is not available.")
        return

    # load annual data
    annual_bs = pd.read_csv(annual_bs_path, index_col=0)
    annual_is = pd.read_csv(annual_is_path, index_col=0)
    annual_cf = pd.read_csv(annual_cf_path, index_col=0)

    ratios = compute_all_ratios(annual_bs, annual_is, annual_cf)
    return ratios
