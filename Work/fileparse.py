# fileparse.py
import csv
import pdb

def parse_csv(filename, select=None,types=None, has_headers=False, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f,delimiter=delimiter)

        # Read the file headers
        headers = next(rows) if has_headers else []
        
        if select:
            indices = [headers.index(colname) for colname in select ]
        
        records = []
        for row in rows:
            
            if not row:    # Skip rows with no data
                continue
            if select:
                row = [row[index] for index in indices]             
            if types:
                row = [func(val) for func,val in zip(types,row)] 
                
            records.append(row)
    return records

if __name__ == '__main__':
    shares_held = parse_csv('Data/prices.csv', types=[str,float],delimiter=',')