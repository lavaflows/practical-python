# report.py
#
# Exercise 2.4

import csv
import sys
from typing import List

def read_portfolio(filename:str):
    '''Read a portfolio'''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)

        portfolio = []
        for row in rows:
            holding = dict(zip(header,row))
            try:
                portfolio.append(holding)
            except ValueError:
                print(f'Error handling: {row}')
        return portfolio
            
def read_prices(filename:str)->dict:
    prices = {}
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        for line in rows:
            try:
                prices[line[0]] = float(line[1])
            except IndexError:
                print(f'Error encountered: {line}')
    return prices


def make_report(portfolio,prices)->List[tuple]:
    report = []
    for holding in portfolio:
        change = float(prices[holding['name']]) - float(holding['price'])
        data = (holding['name'],int(holding['shares']),float(prices[holding['name']]), change)
        report.append(data)
    return report
    




if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
        pricename = 'Data/prices.csv'
    
    portfolio = read_portfolio(filename)
    prices = read_prices(pricename)
    report = make_report(portfolio,prices)

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
    for s in portfolio:
        total_cost += int(s['shares'])*float(s['price'])
        curr_price += float(prices[s['name']])*int(s['shares'])
    print(f'Total Cost: {total_cost}\nCurrent Price: {curr_price:0.2f}\nGain/Loss: {curr_price-total_cost:0.2f}')



