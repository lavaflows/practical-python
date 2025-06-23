# Find logs and detect and open
# Demonstration of using generators for log searching and printing/collection

from pathlib import Path
import gzip
import bz2

def gen_open(paths):    
    for path in paths:
        print(f'Currently reading: {path}')
        if path.suffix == '.gz':
            yield gzip.open(path,'rt')
        elif path.suffix == '.bz2':
            yield bz2.open(path,'rt')
        else:
            yield open(path,'rt')

def gen_cat(sources):
    for src in sources:
        for item in src:
            yield item

lognames = Path('/').rglob('*.log')
logfiles = gen_open(lognames)
loglines = gen_cat(logfiles)


if __name__ == '__main__':
    for i in range(30):
        print(loglines.__next__())