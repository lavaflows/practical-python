import report

portfolio = list(report.read_portfolio('Data/portfolio.csv'))
portfolio.sort(key=lambda s: s.price,reverse=True)
for s in portfolio:
	print(s)

