from follow import follow


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


lines = follow('Data/stocklog.csv')
ibm = filematch(lines, 'IBM')
for line in ibm:
    print(line)