# coding:utf-8

import math


class UpDownHiking():

    def __init__(self):
        self = self

    def maxHeight(self, N, A, B):
        dayA_float = float(N) * float(B) / (float(A) + float(B))
        a = int(round(dayA_float, 0))
        if a == 0:
            a = 1
        elif a == N:
            a = N - 1
        b = int(N - a)
        if a * A - b * B >= 0:
            if a * A - b * B < A:
                return b * B
            else:
                return (a - 1) * A
        elif a * A - b * B < 0:
            if b * B - a * A < B:
                return a * A
            else:
                return (b - 1) * B


up = UpDownHiking()
# answer = up.maxHeight(3, 7, 10)
# print answer
# answer = up.maxHeight(5, 40, 30)
# print answer
# answer = up.maxHeight(2, 50, 1)
# print answer
# answer = up.maxHeight(3, 42, 42)
# print answer
# answer = up.maxHeight(20, 7, 9)
# print answer
answer = up.maxHeight(7, 25, 45)
print answer
