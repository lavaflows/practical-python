# report.py
#
# Exercise 2.4

import csv
import sys
import pdb
from pprint import pprint 

def read_portfolio(filename: str) -> list:
    'Reads a portfolio file and returns total amount paid as a float.'
    with open(filename, 'rt') as file:
        rows = csv.reader(file)

        headers = next(rows)     

        portfolio = []
        for line_no,row in enumerate(rows,start=1):
            record = dict(zip(headers,row))
            try:
                stock = {
                        'name': record['name'],
                        'shares': int(record['shares']),
                        'price': float(record['price'])
                        }
            except ValueError as err:
                print(f'Row {line_no}: Failed with {err}')
                print(f'Row {line_no}: Unable to process: {row}')
                        
            portfolio.append(stock)          
        
    return portfolio

def read_prices(filename: str) -> dict:
    'Read prices and returns a dictionary'
    
    prices = {}
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data:
            if row:
                prices[row[0]] = float(row[1])
            else:
                continue

    return prices
        

def gain_loss(prices:dict, portfolio:dict) -> None:
    'Compute portfolio assets and gains/loss'
    
    total_asset = 0.0
    curr_price = 0.0
    for holding in portfolio:
        total_asset += holding['shares'] * holding['price']
        curr_price += prices[holding['name']] * holding['shares']
    
    profit = curr_price - total_asset
    print(f'Total Assets: {round(total_asset,2)}')
    print(f'Current Value: {round(curr_price,2)}')
    print(f'Gains/Loss: {round(profit,2)}\n')

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




        

if __name__ == '__main__':

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    portfolio = read_portfolio(filename)
    prices = read_prices('Data/prices.csv')
    gain_loss(prices,portfolio)
    report = make_report(portfolio,prices)

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} ${price:>10.2f} {change:>10.2f}')