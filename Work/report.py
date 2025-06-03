# report.py
#
# Exercise 2.4

import csv
import sys
from fileparse import parse_csv
from typing import List
from collections import Counter

def read_portfolio(filename:str):
    '''Read a portfolio'''
    return parse_csv(filename=filename,
                     select=['name','shares','price'],
                     types=[str,int,float],
                     has_headers=True)
            
def read_prices(filename:str)->List[tuple]:
    '''Read prices'''
    return parse_csv(filename=filename,
                      has_headers=False)


def make_report(portfolio:List[dict],prices:dict)->List[tuple]:
    report = []
    for holding in portfolio:
        change = prices[holding['name']] - holding['price']
        data = (holding['name'],int(holding['shares']),float(prices[holding['name']]), change)
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
    total_cost = sum([s['shares']*s['price'] for s in portfolio])
    curr_price = sum(s['shares']*prices[s['name']] for s in portfolio)
    print(f'Total Cost: {total_cost}\nCurrent Price: {curr_price:0.2f}\nGain/Loss: {curr_price-total_cost:0.2f}')

def portfolio_report(filename, pricename):
    '''Runs portfolio report'''

    portfolio = read_portfolio(filename)
    prices = read_prices(pricename)
    # Change prices from a tuple to a key:val dictionary.
    prices = {key:float(val) for key, val in prices}
    report = make_report(portfolio,prices)
    print_report(report,portfolio,prices)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    pricename = 'Data/prices.csv'

    portfolio_report(filename, pricename)



