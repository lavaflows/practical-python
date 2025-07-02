from timethis import timethis

@timethis
def countdown(n):
    while (n > 0):
        n-=1

countdown(100000000)