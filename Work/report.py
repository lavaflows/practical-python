#!/usr/bin/env python3
#  report.py 
#
# Exercise 2.4

import csv
import sys
import pdb
import fileparse
from pprint import pprint 
from stock import Stock
import tableformat

def read_portfolio(filename: str) -> list:
    'Reads a portfolio file and returns total amount paid as a float.'
    with open(filename, 'rt') as lines:
        portfolio = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
    return [Stock(s['name'], s['shares'], s['price']) for s in portfolio]

        
    

def read_prices(filename: str) -> dict:
    'Read prices and returns a dictionary'
    with open(filename, 'rt') as lines:
        return dict(fileparse.parse_csv(lines,types=[str,float], has_headers=False))
        

def gain_loss(prices:dict, portfolio:list) -> None:
    'Compute portfolio assets and gains/loss'
    
    total_asset = 0.0
    curr_price = 0.0

    total_asset = sum([holding.shares*holding.price for holding in portfolio])
    current_price = sum([prices[holding.name] * holding.shares for holding in portfolio])

    
    profit = current_price - total_asset
    
    print()
    print(f'Total Assets  : {total_asset:<10.2f}')
    print(f'Current Value : {current_price:<10.2f}')
    print(f'Gains/Loss    : {profit:<10.2f}\n')

def make_report(portfolio:list, prices:dict) -> list:
    '''Takes a list of stocks and dictionary of prices as input
       Returns a list of tuples containing the rows       
    '''

    report = []
    for holding in portfolio:
        current_price = prices.get(holding.name)
        purchase_price = holding.price
        record = (holding.name, holding.shares, current_price, current_price-purchase_price)
        report.append(record)
    
    return report

def print_report(reportdata: list, formatter) -> None:
    '''Prints a report'''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename: str, prices_filename:str, format:str)-> None:
    'Create and print portfolio'

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio,prices)

    
    match format:
        case 'csv':
            formatter = tableformat.CSVTableFormatter()
        case 'html':
            formatter = tableformat.HTMLTableFormatter()
        case 'txt':
            formatter = tableformat.TextTableFormatter()
        case _:
            formatter = tableformat.TextTableFormatter()

    
    print_report(report,formatter)
    gain_loss(prices,portfolio)

def main(argv):

    if len(sys.argv) == 4:
        portfolio_filename = argv[1]
        prices_filename = argv[2]
        format = argv[3]
    else:
        portfolio_filename = 'Data/portfolio.csv'
        prices_filename = 'Data/prices.csv'
        format = 'txt'
    
    portfolio_report(portfolio_filename, prices_filename, format)

        

if __name__ == '__main__':    
    main(sys.argv)

   