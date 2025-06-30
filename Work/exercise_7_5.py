import report
<<<<<<< HEAD
portfolio = list(report.read_portfolio('Data/portfolio.csv'))
portfolio.sort(key=lambda s: s.name)
for s in portfolio:
        print(s)
=======

portfolio = list(report.read_portfolio('Data/portfolio.csv'))
portfolio.sort(key=lambda s: s.price,reverse=True)
for s in portfolio:
	print(s)
>>>>>>> 3fe59a750c86a0ad8fa64f06b19ccfbae4d4ec4b

