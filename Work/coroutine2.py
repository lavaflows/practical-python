import time

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.__next__()
        return cr
    return start

def follow(filename, target):
    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                time.sleep(0.1)
                continue
            target.send(line)

@coroutine
def printer():
    try:
        while True:
            line = (yield)
            print(line)
    except GeneratorExit:
        pass

@coroutine
def broadcast(targets):
    try:
        while True:
            item = (yield)
            for target in targets:
                target.send(item)
    except GeneratorExit:
        pass
            
if __name__ == '__main__':
    follow('Data/stocklog.csv', broadcast([printer(),printer()]))


