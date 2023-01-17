# typedproperty2.py

import time
def typedproperty(name:str, expected_type):
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self,value):
        if not isinstance(value,expected_type):
            raise TypeError(f'Expected type: {expected_type}')
        setattr(self, private_name, value)    
    return prop

String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)


if __name__ == '__main__':
    
    class Stock:

        name = String('name')
        shares = Integer('shares')
        price = Float('price')

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

        def sell(self, num_shares):
            if not isinstance(num_shares, int):
                raise TypeError(f'Expected integer')
            self.shares -= num_shares

        @property
        def cost(self):
            return self.shares * self.price
        
    s = Stock('GOOG', 100, 490.1)


def timethis(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__}: {end-start:0.5f}')
        return result
    return wrapper