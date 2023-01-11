import os
import time
import report
import csv
def follow(filename):

    f = open(filename, 'r')
    f.seek(0,os.SEEK_END)

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    portfolio = report.read_portfolio('Data/portfolio.csv')
    for data in follow('Data/stocklog.csv'):
        row = data.split(',')
        name = row[0].strip('"')
        price = float(row[1])
        change = float(row[4])
        
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
        