# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

# tableformat.py

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
# tableformat.py

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format
    '''
    def headings(self, headers):
        to_print = ''
        for index,h in enumerate(headers,1):
            if index == 1:
                to_print += '<tr><th>'+ h + '</th>'
            else:
                to_print +=  '<th>' + h + '</th>'
        print(to_print+'</tr>')
    def row(self, rowdata):
        to_print = ''
        for index,h in enumerate(rowdata,1):
            if index == 1:
                to_print += '<tr><td>'+ h + '</td>'
            else:
                to_print +=  '<td>' + h + '</td>'
        print(to_print+'</tr>')

def create_formatter(format):
    match format:
        case 'csv':
            formatter = CSVTableFormatter()
        case 'html':
            formatter = HTMLTableFormatter()
        case 'txt':
            formatter = TextTableFormatter()
        case _:
            formatter = TextTableFormatter()
    return formatter

def print_table(portfolio:list, fields:list, formatter):

    formatter.headings(fields)
    for stock in portfolio:
        rowdata = []
        for field in fields:
            rowdata.append(str(getattr(stock,field)))   
        formatter.row(rowdata)