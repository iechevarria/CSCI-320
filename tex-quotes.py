import fileinput

if __name__ == '__main__':
	for line in fileinput.input():
		df = True
		for i in range(len(line) + line.count('"')):
			if line[i] == '"':
				if df:
					line = line[:i] + '``' + line[i+1:]
				else: 
					line = line[:i] + "''" + line[i+1:]
				df =  not df
		print line,