# coding: utf-8

import math
import string
import itertools
import collections
import re
import array
import bisect
from fractions import gcd


P = 1000000 + 7


class PowerEquationEasy(object):

    def count(self, n):
        r = (2 * n - 1) * n % P
        print r
        x = 1
        while x ** 2 <= n:
            x += 1
            y = x
            b = 0
            while y <= n:
                b += 1
                y *= x
                d = 0
                z = x
                while z <= n:
                    print 'x:', x, 'y:', y, 'z:', z, 'b:', b, 'd:', d
                    d += 1
                    z *= x
                    # 最大公約数
                    if gcd(b, d) == 1 and b != d:
                        r += n / max(b, d)
                        r %= P
        return r

hoge = PowerEquationEasy()
n = 100
print hoge.count(n)
