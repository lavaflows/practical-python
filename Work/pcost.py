#!/usr/bin/env python3
#
# Exercise 1.27
import csv
import sys
import report

def portfolio_cost(filename):
    '''
    Calculate cost of a portfolio.

    Args:
        filename(str): The name of the file.
    
    Returns:
        total_cost(float): The total cost of the portfolio.

    '''
    result = report.read_portfolio(filename)
    
    return sum(row['shares']*row['price'] for row in result)

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile')
        
    filename = sys.argv[1]    
    cost = portfolio_cost(filename)
    print(f'Total cost: {cost}')


if __name__ == '__main__':
    main(sys.argv)
    
