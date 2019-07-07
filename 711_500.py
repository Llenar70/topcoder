# coding:utf-8


import sys
from math import *
import itertools


class OrderedProduct():

    def __init__(self):
        self = self

    def count(self, a):
        a = list(a)
        print a
        a_num = len(a)
        prime_nums = []
        for i in range(1, a_num + 1):
            prime_nums.append(nth_prime(i))
        print prime_nums
        X = long(1)
        for a_i, p_i in zip(a, prime_nums):
            X = X * p_i ** a_i
        print X

        Xpd = prime_decomposition(X)
        print Xpd
        Xlen = len(Xpd)
        seq = 0

        print "answer start"
        # i:  number of group
        for i in range(1, len(Xpd) + 1):
            i_list = range(i)
            print i_list

            zero_pat = 0
            print i
            if i != 1:
                for j in range(1, i):
                    patten1 = list(itertools.combinations(i_list, j))
                    print patten1
                    zero_pat = zero_pat + len(patten1)
            print zero_pat

            patten2 = list(itertools.permutations(i_list))
            print (i ** Xlen - zero_pat) / len(patten2)

            seq = seq + (i ** Xlen - zero_pat) / len(patten2)
            # * len(patten2)

            # patten1 = list(itertools.combinations(Xpd, i + 1))
            # patten2 = list(itertools.permutations(i))
            # print patten1, len(patten1)
            # print patten2, len(patten2)
            # seq = seq + len(patten1) * len(patten2)
            print seq


def nth_prime(N):
    primes = [2]
    n = 1
    while(len(primes) < N):
        n += 2
        m = int(sqrt(n))
        for p in primes:
            if p > m:
                primes.append(n)
                break
            if n % p == 0:
                break
    return primes[-1]


def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

O = OrderedProduct()
answer = O.count((1, 1, 1, 1, 1))
print answer
