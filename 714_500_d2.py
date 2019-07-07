# coding:utf-8


class RemovingParenthesis():

    def __init__(self):
        self = self

    def countWays(self, s):
        answer = 1
        n = 0
        for c in s:
            if c == "(":
                n += 1
                answer *= n
            else:
                n -= 1
            print "n:",n
            print "A:",answer
        return answer

S = RemovingParenthesis()
arr = "((()()()))"

answer = S.countWays(arr)
print answer
