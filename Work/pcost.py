# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename: str) -> float:
    'Reads a portfolio file and returns total amount paid as a float.'
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        
        total_paid = 0
        for line,row in enumerate(rows,start=1):
            record = dict(zip(headers,row))
            try:                
                nshares = int(record['shares'])
                price = float(record['price'])
                total_paid += nshares * price
            except ValueError as error:
                print(f"Row {line}: Couldn't convert:{row}")            
        
    return total_paid

if __name__ == '__main__':

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/missing.csv'

    cost = portfolio_cost(filename)
    print(f'Total paid: {cost}')