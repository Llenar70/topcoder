# coding:utf-8


class RepeatNumberCompare():

    def __init__(self):
        self = self

    def compare(self, x1, k1, x2, k2):
        v1 = ""
        v2 = ""
        for i in range(k1):
            v1 = v1 + str(x1)

        for i in range(k2):
            v2 = v2 + str(x2)

        v1 = long(v1)
        v2 = long(v2)

        if v1 < v2:
            return "Less"
        elif v1 > v2:
            return "Greater"
        else:
            return "Equal"

S = RepeatNumberCompare()
answer = S.compare(1234, 3, 70, 4)
print answer
