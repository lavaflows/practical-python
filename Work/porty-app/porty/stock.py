from .typedproperty import typedproperty, String, Integer, Float

class Stock:
    
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self):
        '''Cost of portfolio'''
        return self.shares * self.price
    def sell(self, num_shares):
        '''Sell shares'''
        if not isinstance(num_shares, int):
            raise ValueError('num_shares should be an integer.') 
        self.shares -= num_shares
            
    
        
    
    

