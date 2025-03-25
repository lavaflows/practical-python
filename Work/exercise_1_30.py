import os

def portfolio_cost(filename):
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
        return total_cost

if __name__ == '__main__':
    filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print(f'Total cost: {cost}')
