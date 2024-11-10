from turtle import down
import click

from src.util import *
from src.search import *
from src.download import *
from src.analysis import *

category_choices = ['economy', 'ticker']
country_choices = ['usa', 'canada']

@click.group()
def cli():
    pass

@cli.command()
@click.option('--category', type=click.Choice(category_choices), required=True, help="Category of data to search")
@click.option('--country', type=click.Choice(country_choices), required=True, help="Country to search data")
@click.argument('query')
def search(category: str, country: str, query: str) -> None:
    if category == 'economy' and country == 'usa':
        print(f"Search data for {query} in {country}")
        search_economy(query)

    elif category == 'ticker' and country == 'usa':
        print(f"Search data for {query} in {country}")
        search_ticker(query)

    elif category == 'economy' and country == 'canada':
        print(f"Search data for {query} in {country}")
    elif category == 'ticker' and country == 'canada':
        print(f"Search data for {query} in {country}")
    else:
        print("Invalid category or country.")

@cli.command()
@click.option('--category', type=click.Choice(category_choices), required=True, help="Category of data to download")
@click.option('--country', type=click.Choice(country_choices), required=True, help="Country to download data")
@click.argument('id')

@click.option('--annual', is_flag=True, help="Download annual data")
@click.option('--quarterly', is_flag=True, help="Download quarterly data")
@click.option('--prices', is_flag=True, help="Download intraday stock price data")
def download(category: str, country: str, id: str, annual: bool, quarterly: bool, prices: bool) -> None:
    if category == 'economy':
        if country == 'usa':
            df = download_economy(id)
            export(df, f"{FRED_DIR}{id}.csv")

        elif country == 'canada':
            print(f"Download {id} data for {country}")

    elif category == 'ticker':
        path = f"{TICKER_DIR}{id}/"
        if not os.path.exists(path):
            os.makedirs(path)

        if annual:
            report = download_ticker(id, "annual")
            
            for key in report:
                export(report[key], f"{path}annual_{key}.csv")

        elif quarterly:
            report = download_ticker(id, "quarterly")
            
            for key in report:
                export(report[key], f"{path}quarterly_{key}.csv")
        
        elif prices:
            data = download_stock(id)
            if data is not None:
                export(data, f"{path}prices.csv")

        else:
            print(f"Download all data for {id}")

if __name__ == '__main__':
    cli()