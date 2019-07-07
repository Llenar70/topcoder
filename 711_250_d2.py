# coding:utf-8

import numpy as np


class SquareMaking():

    def __init__(self):
        self = self

    def getMinimalPrice(self, a, b, c, d):
        list_answer = []
        abcd = [a, b, c, d]
        data = np.array(abcd)
        med = np.median(data)
        answer = (abs(a - med) + abs(b - med) + abs(c - med) + abs(d - med))
        return int(answer)

S = SquareMaking()
a = 705451
b = 751563
c = 608515
d = 994713

answer = S.getMinimalPrice(a, b, c, d)
print answer
