import os

def portfolio_cost(filename:str)-> float:
    with open(filename, 'rt') as f:
        total_cost = 0
        for row, line in enumerate(f):  
            if row == 0:
                continue         
            try:
                data = line.split(',')
                shares = int(data[1])
                price = float(data[2])
                total_cost += shares * price
            except ValueError as error:
                print(f'Failed to parse: {line}')
        return total_cost           



if __name__ == "__main__":
    filename = 'Data/missing.csv'
    total_cost = portfolio_cost(filename)
    print(f'Total Cost: {total_cost}')
    