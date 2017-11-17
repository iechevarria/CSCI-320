import fileinput

def perfectString(k):
    arr = []
    for i in range(1, k):
        if k % i == 0:
            arr.append(i)
    to_return = str(k)
    if sum(arr) == k:
        to_return += ' ='
        for i in range(len(arr) - 1):
            to_return += ' ' + str(arr[i]) + ' +'
        to_return += ' ' + str(arr[len(arr) - 1])
    else:
        to_return += ' is NOT perfect.'
    return to_return


if __name__ == '__main__':
    for line in fileinput.input():
        if line != -1:
            print(perfectString(int(line)))
