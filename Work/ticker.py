# ticker.py

from follow import follow
import csv

def select_columns(rows, indices):
	for row in rows:
		yield [row[index] for index in indices]
		
def parse_stock_data(lines):
	rows = csv.reader(lines)
	rows = select_columns(rows, [0,1,4])
	rows = convert_types(rows, [str,float,float])
	rows = make_dict(rows, ['name','price','change'])
	return rows

def convert_types(rows, types):
	for row in rows:
		yield [fun(val) for fun,val in zip(types,row)]

def make_dict(rows, headers):
	for row in rows:
		yield {name:val for name,val in zip(headers,row)}

def filter_names(rows, names):
	for row in rows:
		if row['name'] in names:
			yield row

def ticker(portfile:str, logfile:str, fmt:str):
	import report
	from tableformat import create_formatter

	portfolio = report.read_portfolio(portfile)
	lines = follow(logfile)
	rows = parse_stock_data(lines)
	rows = filter_names(rows, portfolio)
	formatter = create_formatter(fmt)
	formatter.headings(['name','price','change'])
	for row in rows:
		formatter.row([row['name'],f"{row['price']}",f"{row['change']}"])	
	

if __name__ == '__main__':
	ticker('Data/portfolio.csv','Data/stocklog.csv','txt')

