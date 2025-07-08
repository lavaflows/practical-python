# fileparse.py
#
# Exercise 3.3
import csv
import logging
from typing import TextIO, List
log = logging.getLogger(__name__)

def parse_csv(file:TextIO, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse iterable into records
    '''
    
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
    

    indices = []
    rows = csv.reader(file, delimiter=delimiter)
    headers = next(rows) if has_headers else []
    # Read the file headers
                
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
            
    
    records = []
    for row_no,row in enumerate(rows):
        if not row: # skip row if no data
            continue
        if select:
            row = [row[index] for index in indices] 
        if types:
            try:
                row = [func(val) for func,val in zip(types,row)] 
            except ValueError as e:
                if not silence_errors:
                    log.warning(f"Row {row_no}: Couldn't convert {row}")
                    log.debug(f"Reason: {e}")
                continue


        record = dict(zip(headers,row)) if headers else tuple(row)
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
    
    print(parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=True))