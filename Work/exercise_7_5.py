import report
portfolio = list(report.read_portfolio('Data/portfolio.csv'))
portfolio.sort(key=lambda s: s.name)
for s in portfolio:
        print(s)

