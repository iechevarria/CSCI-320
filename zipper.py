import copy

class StrMix:
    str1 = ''
    str2 = ''
    str3 = ''
    true_s3 = ''
    rnd2 = None

    def __init__(self, str1, str2, str3, true_s3, rnd2):
        self.str1 = str1
        self.str2 = str2
        self.str3 = str3
        self.true_s3 = true_s3
        self.rnd2 = rnd2

    def get_str1(self):
        return self.str1

    def get_str2(self):
        return self.str2

    def get_str3(self):
        return self.str3

    def get_true_s3(self):
        return self.true_s3

    def is_rnd_2(self):
        return self.rnd2

    def set_rnd_2(self):
        self.rnd2 = True


def zipper(s1, s2, s3):

    x = StrMix(s1, s2, '', s3, False)
    mixStack = []

    while True:
        if x.get_str3() == s3:
            return True

        # prevent length of zero causing error
        if len(x.get_str1()) == 0:
            if x.get_str2()[0] == x.get_true_s3()[0]:
                x = StrMix(x.get_str1(), x.get_str2()[1:], x.get_str3() + x.get_str2()[0], x.get_true_s3()[1:], True)
            else:
                if len(mixStack) == 0:
                    return False
                else:
                    x = mixStack.pop()
        elif len(x.get_str2()) == 0:
            if x.get_str1()[0] == x.get_true_s3()[0]:
                x = StrMix(x.get_str1()[1:], x.get_str2(), x.get_str3() + x.get_str1()[0], x.get_true_s3()[1:], True)
            else:
                if len(mixStack) == 0:
                    return False
                else:
                    x = mixStack.pop()

        # append to stack of bifurcations
        elif (x.get_str1()[0] == x.get_true_s3()[0]) and (x.get_str2()[0] == x.get_true_s3()[0]):
            if x.is_rnd_2():
                x = StrMix(x.get_str1(), x.get_str2()[1:], x.get_str3() + x.get_str2()[0], x.get_true_s3()[1:], True)
            else:  
                b = x.deepCopy()
                b.set_rnd_2()
                mixStack.append(b)
                x = StrMix(x.get_str1()[1:], x.get_str2(), x.get_str3() + x.get_str1()[0], x.get_true_s3()[1:], True)

        # make the only possible move
        elif x.get_str1()[0] == x.get_true_s3()[0]:
            x = StrMix(x.get_str1()[1:], x.get_str2(), x.get_str3() + x.get_str1()[0], x.get_true_s3()[1:], True)
        elif x.get_str2()[0] == x.get_true_s3()[0]:
            x = StrMix(x.get_str1(), x.get_str2()[1:], x.get_str3() + x.get_str2()[0], x.get_true_s3()[1:], True)
        else:
            if len(mixStack) == 0:
                return False
            else:
                x = mixStack.pop()


s1 = "cat"
s2 = "tree"
s3 = "cttaree"

print(zipper(s1, s2, s3))
        