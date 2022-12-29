
import fileparse
import pdb

from stock import Stock

with open('Data/portfolio.csv') as lines:
    portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

portfolio = [Stock(s['name'],s['shares'],s['price']) for s in portdicts]
sum([c.cost() for c in portfolio])
