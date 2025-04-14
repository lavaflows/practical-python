# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename:str):
    '''Read a portfolio'''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)

        portfolio = []
        for row in rows:
            holding = {}
            try:
                holding['name'] = row[0]
                holding['shares'] = int(row[1])
                holding['price'] = float(row[2])
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





if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
        pricename = 'Data/prices.csv'
    
    portfolio = read_portfolio(filename)
    prices = read_prices(pricename)
    
    total_cost = 0.0
    curr_price = 0.0
    for s in portfolio:
        total_cost += s['shares']*s['price']
        curr_price += prices[s['name']]*s['shares']
    print(f'Total Cost: {total_cost}\nCurrent Price: {curr_price:0.2f}\nGain/Loss: {curr_price-total_cost:0.2f}')

