# fileparse.py
import csv
import pdb

def parse_csv(filename:str, select:list=None,types:list=None, has_headers:bool=True, delimiter=',',silence_errors:bool=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f,delimiter=delimiter)

        # Read the file headers

        headers = next(rows) if has_headers else []
        if select and not headers:
            raise RuntimeError("select argument requires column headers")
        
        if select:
            indices = [headers.index(colname) for colname in select ]
        
        records = []
        for rowno, row in enumerate(rows,start=1):
            
            if not row:    # Skip rows with no data
                continue
            if select:
                row = [row[index] for index in indices]             
            if types:
                try:
                    row = [func(val) for func,val in zip(types,row)]
                except ValueError as err:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't covert {row}")
                        print(f"Row {rowno}: {err}")
            if headers:
                record = dict(zip(headers,row))
            else:
                record = tuple(row)

            records.append(record)
    return records

if __name__ == '__main__':
    shares_held = parse_csv('Data/prices.csv', types=[str,int,float],silence_errors=True, has_headers=True)