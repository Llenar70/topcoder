# coding:utf-8

class SquareMaking():

    def __init__(self):
        self = self

    def getMinimalPrice(self, a, b, c, d):
        list_answer = []
        abcd = [a, b, c, d]
        list_answer = []
        for i in abcd:
            answer = 0
            for j in abcd:
                answer = answer + abs(i - j)
            list_answer.append(answer)
        return min(list_answer)

S = SquareMaking()
a = 705451
b = 751563
c = 608515
d = 994713

answer = S.getMinimalPrice(a, b, c, d)
print answer
