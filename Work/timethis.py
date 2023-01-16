import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__}: {end-start:0.5f} seconds')
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    countdown(20000000)
