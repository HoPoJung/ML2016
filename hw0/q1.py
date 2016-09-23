import sys


outputColumn = int(sys.argv[1])
if outputColumn > 10 or outputColumn < 0:
	print 'Input number exeed matrix dimension.'
	sys.exit()
filename = sys.argv[2]
data = []

with open(filename, 'r') as file:
	for line in file:
		part  = line.split();
		for column in range(0, len(part)):
			if column == outputColumn:
				data.append(float(part[column]))

dataSorted = sorted(data)
print data


