import ipdb
import pandas as pd

# Current Ratio
def calculate_current_ratio(bs: pd.DataFrame) -> pd.Series:
    current_assets = bs.loc['us-gaap_AssetsCurrent']
    current_liabilities = bs.loc['us-gaap_LiabilitiesCurrent']
    return current_assets / current_liabilities

# Quick Ratio
def calculate_quick_ratio(bs: pd.DataFrame) -> pd.Series:
    current_assets = bs.loc['us-gaap_AssetsCurrent']
    inventory = bs.loc['us-gaap_InventoryNet']
    current_liabilities = bs.loc['us-gaap_LiabilitiesCurrent']
    return (current_assets - inventory) / current_liabilities

# Gross Margin
def calculate_gross_margin(income_statement: pd.DataFrame) -> pd.Series:
    revenue = income_statement.loc['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax']
    cogs = income_statement.loc['us-gaap_CostOfGoodsAndServicesSold']
    return (revenue - cogs) / revenue

# Operating Margin
def calculate_operating_margin(income_statement: pd.DataFrame) -> pd.Series:
    operating_income = income_statement.loc['us-gaap_OperatingIncomeLoss']
    revenue = income_statement.loc['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax']
    return operating_income / revenue

# Net Profit Margin
def calculate_net_profit_margin(income_statement: pd.DataFrame) -> pd.Series:
    net_income = income_statement.loc['us-gaap_NetIncomeLoss']
    revenue = income_statement.loc['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax']
    return net_income / revenue

# Debt to Equity Ratio
def calculate_debt_to_equity(bs: pd.DataFrame) -> pd.Series:
    total_debt = bs.loc['us-gaap_Liabilities']
    equity = bs.loc['us-gaap_StockholdersEquity']
    return total_debt / equity

# Debt to Assets Ratio
def calculate_debt_to_assets(bs: pd.DataFrame) -> pd.Series:
    total_debt = bs.loc['us-gaap_Liabilities']
    total_assets = bs.loc['us-gaap_Assets']
    return total_debt / total_assets

# Return on Assets (ROA)
def calculate_roa(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    net_income = income_statement.loc['us-gaap_NetIncomeLoss']
    total_assets = bs.loc['us-gaap_Assets']
    return net_income / total_assets

# Return on Equity (ROE)
def calculate_roe(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    net_income = income_statement.loc['us-gaap_NetIncomeLoss']
    equity = bs.loc['us-gaap_StockholdersEquity']
    return net_income / equity

# Operating Cash Flow Ratio
def calculate_operating_cash_flow_ratio(cf: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    operating_cash_flow = cf.loc['us-gaap_NetCashProvidedByUsedInOperatingActivities']
    current_liabilities = bs.loc['us-gaap_LiabilitiesCurrent']
    return operating_cash_flow / current_liabilities

# Free Cash Flow
def calculate_free_cash_flow(cf: pd.DataFrame) -> pd.Series:
    operating_cash_flow = cf.loc['us-gaap_NetCashProvidedByUsedInOperatingActivities']
    capital_expenditures = cf.loc['us-gaap_PaymentsToAcquirePropertyPlantAndEquipment']
    return operating_cash_flow - capital_expenditures

# Cash Ratio
def calculate_cash_ratio(bs: pd.DataFrame) -> pd.Series:
    cash_and_equivalents = bs.loc['us-gaap_CashAndCashEquivalentsAtCarryingValue']
    current_liabilities = bs.loc['us-gaap_LiabilitiesCurrent']
    return cash_and_equivalents / current_liabilities

# Asset Turnover
def calculate_asset_turnover(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    revenue = income_statement.loc['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax']
    total_assets = bs.loc['us-gaap_Assets']
    return revenue / total_assets

# Inventory Turnover
def calculate_inventory_turnover(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    cogs = income_statement.loc['us-gaap_CostOfGoodsAndServicesSold']
    inventory = bs.loc['us-gaap_InventoryNet']
    return cogs / inventory

# Receivables Turnover
def calculate_receivables_turnover(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    try:
        revenue = income_statement.loc['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax']
        receivables = bs.loc['us-gaap_ReceivablesNetCurrent']
        return revenue / receivables
    except:
        # get number of columns in the dataframe
        num_cols = len(income_statement.columns)
        return pd.Series([0] * num_cols, index=income_statement.columns)

# Cash Flow to Debt Ratio
def calculate_cash_flow_to_debt(cf: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    operating_cash_flow = cf.loc['us-gaap_NetCashProvidedByUsedInOperatingActivities']
    total_debt = bs.loc['us-gaap_Liabilities']
    return operating_cash_flow / total_debt

# Working Capital
def calculate_working_capital(bs: pd.DataFrame) -> pd.Series:
    current_assets = bs.loc['us-gaap_AssetsCurrent']
    current_liabilities = bs.loc['us-gaap_LiabilitiesCurrent']
    return current_assets - current_liabilities

# EBITDA Margin
def calculate_ebitda_margin(cf: pd.DataFrame, income_statement: pd.DataFrame) -> pd.Series:
    operating_income = income_statement.loc['us-gaap_OperatingIncomeLoss']
    depreciation_amortization = cf.loc['us-gaap_DepreciationDepletionAndAmortization']
    ebitda = operating_income + depreciation_amortization
    revenue = income_statement.loc['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax']
    return ebitda / revenue

# EBIT Margin
def calculate_ebit_margin(income_statement: pd.DataFrame) -> pd.Series:
    ebit = income_statement.loc['us-gaap_OperatingIncomeLoss']
    revenue = income_statement.loc['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax']
    return ebit / revenue

# Return on Investment (ROI)
def calculate_roi(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    net_income = income_statement.loc['us-gaap_ProfitLoss']
    total_assets = bs.loc['us-gaap_Assets']
    return net_income / total_assets

# Days Sales Outstanding (DSO)
def calculate_dso(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    receivables = bs.loc['us-gaap_ReceivablesNetCurrent']
    revenue = income_statement.loc['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax']
    dso = (receivables / revenue) * 365
    return dso

# Days Inventory Outstanding (DIO)
def calculate_dio(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    inventory = bs.loc['us-gaap_InventoryNet']
    cogs = income_statement.loc['us-gaap_CostOfGoodsAndServicesSold']
    dio = (inventory / cogs) * 365
    return dio

# Days Payables Outstanding (DPO)
def calculate_dpo(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    accounts_payable = bs.loc['us-gaap_AccountsPayableCurrent']
    cogs = income_statement.loc['us-gaap_CostOfGoodsAndServicesSold']
    dpo = (accounts_payable / cogs) * 365
    return dpo

# Cash Conversion Cycle (CCC)
def calculate_ccc(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    dso = calculate_dso(income_statement, bs)
    dio = calculate_dio(income_statement, bs)
    dpo = calculate_dpo(income_statement, bs)
    return dso + dio - dpo

# Interest Coverage Ratio
def calculate_interest_coverage_ratio(income_statement: pd.DataFrame) -> pd.Series:
    ebit = income_statement.loc['us-gaap_OperatingIncomeLoss']
    interest_expense = income_statement.loc['us-gaap_InterestExpense']
    return ebit / interest_expense

# Debt Service Coverage Ratio
def calculate_debt_service_coverage_ratio(income_statement: pd.DataFrame, cf: pd.DataFrame) -> pd.Series:
    operating_cash_flow = cf.loc['us-gaap_NetCashProvidedByUsedInOperatingActivities']
    debt_payments = cf.loc['us-gaap_RepaymentsOfShortTermDebt'] + cf.loc['us-gaap_RepaymentsOfLongTermDebt']
    
    return operating_cash_flow / debt_payments

# Earnings per Share (EPS)
def calculate_eps(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    net_income = income_statement.loc['us-gaap_NetIncomeLoss']
    shares_outstanding = bs.loc['us-gaap_CommonStockValue']
    return net_income / shares_outstanding

# Price to Earnings (P/E) Ratio
def calculate_pe(income_statement: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    net_income = income_statement.loc['us-gaap_NetIncomeLoss']
    shares_outstanding = bs.loc['us-gaap_CommonStockValue']
    price_per_share = net_income / shares_outstanding

    eps = calculate_eps(income_statement, bs)
    return price_per_share / eps

# Price to Book (P/B) Ratio
def calculate_pb(bs: pd.DataFrame) -> pd.Series:
    equity = bs.loc['us-gaap_StockholdersEquity']
    shares_outstanding = bs.loc['us-gaap_CommonStockValue']
    price_per_share = equity / shares_outstanding
    book_value_per_share = equity / shares_outstanding
    return price_per_share / book_value_per_share

# Dividend Yield
# def calculate_dividend_yield(income_statement: pd.DataFrame, share_price: float) -> float:
#     dividends_paid = cf.loc['us-gaap_PaymentsOfDividendsCommonStock']
#     return (dividends_paid / share_price) * 100 if share_price != 0 else 0

# Dividend Payout Ratio
def calculate_dividend_payout_ratio(income_statement: pd.DataFrame, cf: pd.DataFrame) -> pd.Series:
    dividends_paid = cf.loc['us-gaap_PaymentsOfDividendsCommonStock']
    net_income = income_statement.loc['us-gaap_NetIncomeLoss']
    return (dividends_paid / net_income) * 100

# Operating Cash Flow to Liabilities
def calculate_operating_cash_flow_to_liabilities(cf: pd.DataFrame, bs: pd.DataFrame) -> pd.Series:
    operating_cash_flow = cf.loc['us-gaap_NetCashProvidedByUsedInOperatingActivities']
    current_liabilities = bs.loc['us-gaap_LiabilitiesCurrent']
    return operating_cash_flow / current_liabilities

# Capital Expenditures to Depreciation
def calculate_capex_to_depreciation(cf: pd.DataFrame) -> pd.Series:
    capex = cf.loc['us-gaap_PaymentsToAcquirePropertyPlantAndEquipment']
    depreciation = cf.loc['us-gaap_DepreciationDepletionAndAmortization']
    return capex / depreciation

# Revenue Growth Rate
def calculate_revenue_growth_rate(income_statement: pd.DataFrame) -> pd.Series:
    current_revenue = income_statement.loc['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax']
    previous_revenue = income_statement.loc['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax']
    return ((current_revenue - previous_revenue) / previous_revenue) * 100

# Earnings Growth Rate
def calculate_earnings_growth_rate(income_statement: pd.DataFrame) -> pd.Series:
    current_net_income = income_statement.loc['us-gaap_NetIncomeLoss']
    previous_net_income = income_statement.loc['us-gaap_NetIncomeLoss']
    return ((current_net_income - previous_net_income) / previous_net_income) * 100

def compute_all_ratios(bs: pd.DataFrame, income_statement: pd.DataFrame, cf: pd.DataFrame) -> pd.DataFrame:
    ratios = {
        'current_ratio': calculate_current_ratio(bs),
        'quick_ratio': calculate_quick_ratio(bs),
        'gross_margin': calculate_gross_margin(income_statement),
        'operating_margin': calculate_operating_margin(income_statement),
        'net_profit_margin': calculate_net_profit_margin(income_statement),
        'debt_to_equity': calculate_debt_to_equity(bs),
        'debt_to_assets': calculate_debt_to_assets(bs),
        'roa': calculate_roa(income_statement, bs),
        'roe': calculate_roe(income_statement, bs),
        'operating_cash_flow_ratio': calculate_operating_cash_flow_ratio(cf, bs),
        'free_cash_flow': calculate_free_cash_flow(cf),
        'cash_ratio': calculate_cash_ratio(bs),
        'asset_turnover': calculate_asset_turnover(income_statement, bs),
        'inventory_turnover': calculate_inventory_turnover(income_statement, bs),
        'receivables_turnover': calculate_receivables_turnover(income_statement, bs),
        'cash_flow_to_debt': calculate_cash_flow_to_debt(cf, bs),
        "working_capital": calculate_working_capital(bs),
        "ebitda_margin": calculate_ebitda_margin(cf, income_statement),
        "ebit_margin": calculate_ebit_margin(income_statement),
        "roi": calculate_roi(income_statement, bs),
        "dso": calculate_dso(income_statement, bs),
        "dio": calculate_dio(income_statement, bs),
        "dpo": calculate_dpo(income_statement, bs),
        "ccc": calculate_ccc(income_statement, bs),
        "interest_coverage_ratio": calculate_interest_coverage_ratio(income_statement),
        "debt_service_coverage_ratio": calculate_debt_service_coverage_ratio(income_statement, cf),
        "eps": calculate_eps(income_statement, bs),
        "pe": calculate_pe(income_statement, bs),
        "pb": calculate_pb(bs),
        # "dividend_yield": calculate_dividend_yield(income_statement, bs),
        "dividend_payout_ratio": calculate_dividend_payout_ratio(income_statement, cf),
        "operating_cash_flow_to_liabilities": calculate_operating_cash_flow_to_liabilities(cf, bs),
        "capex_to_depreciation": calculate_capex_to_depreciation(cf),
        "revenue_growth_rate": calculate_revenue_growth_rate(income_statement),
        "earnings_growth_rate": calculate_earnings_growth_rate(income_statement)
    }

    ratios_df = pd.DataFrame(ratios)
    ratios_df = ratios_df.T
    return ratios_df