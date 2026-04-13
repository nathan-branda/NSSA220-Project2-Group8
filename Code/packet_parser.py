def parse() :
	packets = [[],[],[],[]]
	for i in range(1,5):
		filename = '../Captures/Node' + str(i) + '_filtered.txt'
		file = open(filename, 'r')
		line = file.readline()

		while line:
			if line[0] == "N":
				line = file.readline()
				fields = line.split()
				packet = {}
				#print(fields)
				packet['num'] = fields[0]
				packet['time'] = fields[1]
				packet['src'] = fields[2]
				packet['dst'] = fields[3]
				packet['len'] = fields[5]
				packet['type'] = fields[8]
				packet['assoc'] = fields[-1][:-1]
				#print(packet)
				packets[i-1].append(packet)
			line = file.readline()
	print('called parse function in packet_parser.py')
	return packets
	