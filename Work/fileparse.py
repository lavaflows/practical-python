# fileparse.py
#
# Exercise 3.3
import csv
import pdb

def parse_csv(filename:str, select=None, types=None, has_headers=False, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename, 'rt') as f:
        indices = []
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else []
        # Read the file headers
        if has_headers:            
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []
        elif select:
            if not silence_errors:
                raise RuntimeError("select arugument requirers column headers.")
        
        records = []
        for row_no,row in enumerate(rows):
            if not row: # skip row if no data
                continue
            if indices and has_headers:
                row = [row[index] for index in indices] 
            if types:
                try:
                    row = [func(val) for func,val in zip(types,row)] 
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {row_no}: Couldn't convert {row}")
                        raise


            record = dict(zip(headers,row)) if has_headers else tuple(row)
            records.append(record)
        
        return records
    
if __name__ == '__main__':
    print(parse_csv('Data/portfoliodate.csv',
                    select=['name','price','date','shares'],
                    types=[str,float,lambda x: tuple(map(int,x.split('/'))),int],
                    has_headers=True,
                    delimiter=','))
    
    print(parse_csv('Data/portfolio.csv',
                    select=['name','price','shares'],
                    types=[str,float,int],
                    has_headers=True,
                    delimiter=','))
    
    print(parse_csv('Data/portfolio.dat',
                    select=['name','price','shares'],
                    types=[str,float,int],
                    has_headers=True,
                    delimiter=' '))
    
    print(parse_csv('Data/portfolioblank.csv',
                    select=['name','price','shares'],
                    types=[str,float,int],
                    has_headers=True,
                    delimiter=','))
    
    print(parse_csv('Data/prices.csv',
                    types=[str,float],
                    delimiter=','))
    print(parse_csv('Data/prices.csv',
                    types=[str,float],
                    select=['name','price'],
                    delimiter=',',
                    silence_errors=True))
    
    print(parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=True))