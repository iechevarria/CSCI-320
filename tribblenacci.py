import fileinput

if __name__=="__main__":
    t_ct = [1, 1, 2, 4]
    for i in range(65):
        t_ct.append(t_ct[-1] + t_ct[-2] + t_ct[-3] + t_ct[-4])
    first = True
    for line in fileinput.input():
        if first:
            first = False
        else:
            print(t_ct[int(line)])