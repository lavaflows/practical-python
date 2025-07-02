#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

import csv
import sys
import tableformat
from fileparse import parse_csv
from typing import List
from collections import Counter
from portfolio import Portfolio

from stock import Stock

def read_portfolio(filename:str, **opts)->List[Stock]:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, price.
    '''
    with open(filename, 'rt') as lines:
        port = Portfolio.from_csv(lines)

    return port
            
def read_prices(filename:str)->List[tuple]:
    '''
    Read prices file into a dictionary mapping
    '''
    with open(filename, 'rt') as lines:
        return parse_csv(lines, has_headers=False)


def make_report(portfolio:List[Stock]=None,prices:dict=None)->List[tuple]:
    report = []
    for holding in portfolio:
        change = prices[holding.name] - holding.price
        data = (holding.name,int(holding.shares),float(prices[holding.name]), change)
        report.append(data)
    return report
    

def print_report(report:List[dict]=None, portfolio:List[dict]=None, prices:dict=None, formatter:tableformat.TableFormatter=None):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
    
    total_cost = 0.0
    curr_price = 0.0
    total_cost = sum([s.cost for s in portfolio])
    curr_price = sum(s.shares*prices[s.name] for s in portfolio)
    print(f'\n{"":->18}{"Summary":-<25}\n')
    print(f'Total Cost: {total_cost}\nCurrent Price: {curr_price:0.2f}\nGain/Loss: {curr_price-total_cost:0.2f}')

def portfolio_report(filename, pricename, fmt='txt'):
    '''Runs portfolio report'''

    portfolio = read_portfolio(filename)
    prices = read_prices(pricename)
    # Change prices from a tuple to a key:val dictionary.
    prices = {key:float(val) for key, val in prices}
    report = make_report(portfolio,prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report,portfolio,prices, formatter)

def main(argv):
    if len(argv) !=4:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    fmt = argv[3]
    
    portfolio_report(portfile, pricefile, fmt)

if __name__ == '__main__':
    main(sys.argv)
    

    



