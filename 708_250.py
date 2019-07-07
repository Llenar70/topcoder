# coding:utf-8


class SafeBetting():

    def __init__(self):
        self = self

    def minRounds(self, a, b, c):
        bet = b - a
        print bet
        B = 0
        money = b
        while c > money:
            print B
            money = money + bet * (2 ** B)
            print money
            B = B + 1
        return B