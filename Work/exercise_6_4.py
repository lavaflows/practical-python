# exercise_6_4.py
import os
import sys

def filematch(filename, substr):
    with open(filename, 'rt') as f:
        for line in f:
            if substr in line:
                yield line
def main(argv):
    substr =  argv[1] if len(argv) == 2 else 'IBM'
    
    for line in filematch('Data/portfolio.csv',substr):
        print(line, end='')

if __name__ == "__main__":
    main(sys.argv)
       
