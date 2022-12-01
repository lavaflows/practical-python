
import sys
import csv
import pdb

def read_stocks(filename:str)->None:
    'Read file and return stocks'

    
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        header = next(rows)
        types = [str, float, str, str, float, float, float, float, int]
        

        record = []
        
        converted = [[func(val) for func,val in zip(types,row)] for row in rows]
        record.append(dict(zip(header,converted)))

        return record


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) > 2:
        filename = argv[2]
    else:
        filename = 'Data/dowstocks.csv'
    
    h = read_stocks(filename)