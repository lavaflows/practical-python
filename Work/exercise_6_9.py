# exercise_6_9.py

def filematch(lines,substr):
	for line in lines:
		if substr in line:
			yield line

from follow import follow
import csv
lines = follow('Data/stocklog.csv')
rows = csv.reader(lines)
for row in rows:
	print(row)
