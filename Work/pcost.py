# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        total_cost = 0
        rows = csv.reader(f)
        header = next(rows)

        for row,line in enumerate(rows):   
            record = dict(zip(header,line))    
            try:

                shares = int(record['shares'])
                price = float(record['price'])
                total_cost+= shares * price
            except ValueError:
                print(f'Row {row}: Error parsing {line}')
            
        return total_cost

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/missing.csv'
    
    cost = portfolio_cost(filename)
    print(f'Total cost: {cost}')
