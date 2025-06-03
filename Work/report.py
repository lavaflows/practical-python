#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

import csv
import sys
from fileparse import parse_csv
from typing import List
from collections import Counter
from stock import Stock

def read_portfolio(filename:str)->List[Stock]:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, price.
    '''
    with open(filename, 'rt') as lines:
        portdicts = parse_csv(lines, select=['name','shares','price'], types=[str,int,float], has_headers=True)

    portfolio = [Stock(s['name'],s['shares'],s['price']) for s in portdicts]
    return portfolio
            
def read_prices(filename:str)->List[tuple]:
    '''
    Read prices file into a dictionary mapping
    '''
    with open(filename, 'rt') as lines:
        return parse_csv(lines, has_headers=False)


def make_report(portfolio:List[Stock],prices:dict)->List[tuple]:
    report = []
    for holding in portfolio:
        change = prices[holding.name] - holding.price
        data = (holding.name,int(holding.shares),float(prices[holding.name]), change)
        report.append(data)
    return report
    

def print_report(report:List[dict], portfolio:List[dict], prices:dict):
    once = True    
    for name,shares,price,change in report:
        if once:
            headers = ('Name', 'Shares', 'Price', 'Change')
            print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
            print(f'{"":->10s} {"":->10s} {"":->10s} {"":->10s}')
            once = False

        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
    
    total_cost = 0.0
    curr_price = 0.0
    total_cost = sum([s.cost() for s in portfolio])
    curr_price = sum(s.shares*prices[s.name] for s in portfolio)
    print(f'\n{"":->18}{"Summary":-<25}\n')
    print(f'Total Cost: {total_cost}\nCurrent Price: {curr_price:0.2f}\nGain/Loss: {curr_price-total_cost:0.2f}')

def portfolio_report(filename, pricename):
    '''Runs portfolio report'''

    portfolio = read_portfolio(filename)
    prices = read_prices(pricename)
    # Change prices from a tuple to a key:val dictionary.
    prices = {key:float(val) for key, val in prices}
    report = make_report(portfolio,prices)
    print_report(report,portfolio,prices)

def main(argv):
    if len(argv) !=3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    
    portfolio_report(portfile, pricefile)

if __name__ == '__main__':
    main(sys.argv)
    

    



