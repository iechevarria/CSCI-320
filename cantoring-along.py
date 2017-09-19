import fileinput

def cantor(order):
	prev = '-'
	for i in range(1, order + 1):
		prev = prev + 3**(i-1) * ' ' + prev
	return prev

if __name__ == '__main__':
	arr = []
	for line in fileinput.input():
		arr.append(line.strip('\n'))
	for i in range(len(arr)):
		print(cantor(int(arr[i])))