# typedproperty.py

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

    # Define class Stock
    # Create Stock instance
    # Try to create with different expected type.
    
    # Demonstrates closure and reducing code repetition by returning a type checker for each attribute
    # in the form of a @property and prop.setter function.

    class Stock:

        name = String('name')
        shares = Integer('shares')
        price = Float('price')

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

        def sell(self, num_shares):
            '''Sell shares'''
            if not isinstance(num_shares, int):
                raise TypeError(f'Expected int: {num_shares}')
            self.shares -= num_shares
        
        @property
        def cost(self):
            '''Cost of portfolio'''
            return self.shares * self.price

    s = Stock('GOOG', 100, 92.1)
    s.shares = 200