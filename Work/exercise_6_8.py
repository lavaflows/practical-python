# exercise_6_8.py

def filematch(lines, substr):
	for line in lines:
		if substr in line:
			yield line


from follow import follow

lines = follow('Data/stocklog.csv')
ibm = filematch(lines, 'IBM')
for line in ibm:
	print(line)

			
