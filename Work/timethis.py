# timethis.py

import time
def timethis(func):
    def timewrap(*args,**kwargs):
        start = time.time()
        results = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__}: Took {end-start} time')
        return results
    return timewrap

@timethis
def loop(count):
    for i in range(count):
        pass

if __name__ == '__main__':
    loop(1000)