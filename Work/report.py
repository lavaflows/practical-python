# report.py
#
# Exercise 2.4

import csv
import sys
import pdb 

def read_portfolio(filename: str) -> list:
    'Reads a portfolio file and returns total amount paid as a float.'
    with open(filename, 'rt') as file:
        rows = csv.reader(file)

        headers = next(rows)     

        portfolio = []
        for row in rows:
            stock = {
                        'name': row[0],
                        'shares': float(row[1]),
                        'price': float(row[2])
                        }
                        
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
    print(f'Total Assets: {round(total_asset,2)}\nGains/Loss: {round(profit,2)}')
    

        

if __name__ == '__main__':

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    portfolio = read_portfolio(filename)
    prices = read_prices('Data/prices.csv')