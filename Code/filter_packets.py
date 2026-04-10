import re
def filter() :
	for i in range(1,5):
		filename = '../Captures/Node' + str(i) + '.txt'
		file = open(filename,'r')
		output_filename = '../Captures/Node' + str(i) + '_filtered.txt'
		output = open(output_filename, 'w')
		line = file.readline()
		header = line

		while line:
			if line[0] == "N":
				line = file.readline()
				if re.search('Echo', line):
					output.write(header)
					output.write(line)
					line = file.readline()
					output.write(line)
					line = file.readline().strip()
					while line:
						output.write(line + '\n')
						line = file.readline().strip()
					output.write('\n')
			line = file.readline()
		file.close()
	print('called filter function in filter_packets.py')
filter()
	
