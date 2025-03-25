import os

filename = 'Data/portfolio.csv'

with open(filename, 'rt') as f:
    total_cost = 0
    for row,line in enumerate(f):
        data = line.split(',')
        try:
            shares = int(data[1])
            price = float(data[2])
            total_cost += int(data[1])*float(data[2])
        except ValueError:
            print(f"Couldn't parse: {line}")
        
    
    print(f'Total cost: {total_cost}')
