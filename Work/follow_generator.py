
import os
import time

def follow(filename):    
    with open(filename, 'r') as file:
        file.seek(0,os.SEEK_END)
        while True:
            line = file.readline()
            if line == '':
                time.sleep(0.1)
                continue
            yield line

if __name__== '__main__':
    for rowno, row in enumerate(follow('Data/stocklog.csv'),1):
        print(f'Row {rowno}: {row}')
