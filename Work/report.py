# report.py
#
# Exercise 2.4

import csv
import sys
import pdb
import fileparse
from pprint import pprint 


def read_portfolio(filename: str) -> list:
    'Reads a portfolio file and returns total amount paid as a float.'
    # with open(filename, 'rt') as file:
    #     rows = csv.reader(file)

    #     headers = next(rows)     

    #     portfolio = []
    #     for line_no,row in enumerate(rows,start=1):
    #         record = dict(zip(headers,row))
    #         try:
    #             stock = {
    #                     'name': record['name'],
    #                     'shares': int(record['shares']),
    #                     'price': float(record['price'])
    #                     }
    #         except ValueError as err:
    #             print(f'Row {line_no}: Failed with {err}')
    #             print(f'Row {line_no}: Unable to process: {row}')
                        
    #         portfolio.append(stock)          
        
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename: str) -> dict:
    'Read prices and returns a dictionary'
    # prices = {}
    # with open(filename, 'r') as file:
    #     data = csv.reader(file)
    #     for row in data:
    #         if row:
    #             prices[row[0]] = float(row[1])
    #         else:
    #             continue

    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))
        

def gain_loss(prices:dict, portfolio:dict) -> None:
    'Compute portfolio assets and gains/loss'
    
    total_asset = 0.0
    curr_price = 0.0

    total_asset = sum([holding['shares']*holding['price'] for holding in portfolio])
    current_price = sum([prices[holding['name']] * holding['shares'] for holding in portfolio])

    
    profit = current_price - total_asset
    print(f'Total Assets  : {total_asset:<10.2f}')
    print(f'Current Value : {current_price:<10.2f}')
    print(f'Gains/Loss    : {profit:<10.2f}\n')

def make_report(portfolio:list, prices:dict) -> list:
    '''Takes a list of stocks and dictionary of prices as input
       Returns a list of tuples containing the rows       
    '''

    report = []
    for holding in portfolio:
        current_price = prices.get(holding['name'])
        purchase_price = holding['price']
        record = (holding['name'], holding['shares'], current_price, current_price-purchase_price)
        report.append(record)
    
    return report

def print_report(report: list) -> None:
    'Prints a report'
    print('\n')
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} ${price:>10.2f} {change:>10.2f}')

    print('\n')


def portfolio_report(portfolio_filename: str, prices_filename:str)-> None:
    'Create and print portfolio'

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio,prices)

    print_report(report)
    gain_loss(prices,portfolio)

def main(argv):

    if len(sys.argv) == 3:
        portfolio_filename = argv[1]
        prices_filename = argv[2]
    else:
        portfolio_filename = 'Data/portfolio.csv'
        prices_filename = 'Data/prices.csv'
    
    portfolio_report(portfolio_filename, prices_filename)

        

if __name__ == '__main__':    
    main(sys.argv)

   