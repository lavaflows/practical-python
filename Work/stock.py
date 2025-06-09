#!/usr/env/python3

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
    def cost(self):
        return self.shares * self.price
    def sell(self, shares:int):
        self.shares = self.shares - shares if shares <= self.shares else 0

if __name__=='__main__':
    a = Stock('GOOG',100,490.10)
    print(a.cost())
    