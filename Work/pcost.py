# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    '''
    Calculate cost of a portfolio.

    Args:
        filename(str): The name of the file.
    
    Returns:
        total_cost(float): The total cost of the portfolio.

    '''
    with open(filename, 'rt') as file:
        total_cost = 0.0
        data = csv.reader(file)
        header = next(data)
    
        for row_no, line in enumerate(data):
            record = dict(zip(header,line))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares*price
            except ValueError as msg:
                print(f'{row_no}: {line} couldnt load')
        return total_cost
    

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/missing.csv'
    
    cost = portfolio_cost(filename)
    print(f'Total cost: {cost}')
