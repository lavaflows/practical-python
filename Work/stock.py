class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return 'Stock('+','.join([self.name,str(self.shares),str(self.price)])+')'

    def cost(self):
        '''Cost of portfolio'''
        return self.shares * self.price
    def sell(self, num_shares):
        '''Sell shares'''
        if isinstance(num_shares, int):
            self.shares -= num_shares
        else:
            raise ValueError('num_shares should be an integer.')
    
        
    
    

