# Read in prices
from pprint import pprint
def read_prices(filename:str)->dict:
    prices = {}
    with open(filename,'rt') as f:
        for line in f:
            try:
                row = line.split(',')
                prices[row[0]] = float(row[1])
            except IndexError:
                print(f'Error encountered: {row}')
    return prices


if __name__ == "__main__":
    filename = 'Data/prices.csv'
    prices = read_prices(filename)
    pprint(prices)
