#ticker.py

from follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func,val in zip(types,row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers,row))

def filter_symbols(rows, symbols):
    for row in rows:
        if row['name'] in symbols:
            yield row
    

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows,[str, float, float])
    rows = make_dicts(rows, ['name','price', 'change'])  

    return rows

def ticker(portfile, logfile, fmt):
    import tableformat

    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(logfile)
    formatter = tableformat.create_formatter(fmt)

    for row in rows:
        tableformat.print_table(portfolio)


    

if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)