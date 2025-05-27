from typing import List
import csv

def parse_portfolio(filename:str) -> List[dict]:

    types = [str, float, lambda x: tuple(map(int,x.split('/'))), str, float, float, float, float, int]

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        record = []
        for row in rows:
            converted = [func(val) for func, val in zip(types,row)]
            record.append({name:val for name, val in zip(header,converted)})        
    return record


if __name__ == '__main__':
    result = parse_portfolio('Data/dowstocks.csv')
    print(result[0])