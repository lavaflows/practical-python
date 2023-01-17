# fileparse.py
import csv
import io
from pprint import pprint

import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select:list=None,types:list=None, has_headers:bool=True, delimiter=',',silence_errors:bool=False):
    '''
    Parse a CSV file into a list of records
    '''
    # Read the file headers

    if isinstance(lines,str):
        raise RuntimeError("lines must be a iterable file/io stream.")

    rows = csv.reader(lines, delimiter=delimiter)

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
                    log.warning("Row %d: Couldn't convert %s", rowno,row)
                    log.debug("Row %d: %s",rowno, err)
                continue
        if headers:
            record = dict(zip(headers,row))
        else:
            record = tuple(row)
        records.append(record)

    return records

if __name__ == '__main__':

    filename = 'Data/portfolio.csv'
    with open(filename, 'rt') as lines:
        shares_held = parse_csv(lines, types=[str,int,float],silence_errors=True, has_headers=True)
        pprint(shares_held)