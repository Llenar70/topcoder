# coding:utf-8
import copy


class RemovingParenthesis():

    def __init__(self):
        self = self

    def countWays(self, s):
        return self.deletekakko(0, list(s))

    def deletekakko(self, answer, lists):
        a = 0
        if lists == "":
            return answer
        lists.pop(0)
        i = 0
        for n in lists:
            if n == ")":
                copi = copy.deepcopy(lists)
                copi.pop(i)
                if self.kakko(copi):
                    a += 1
                    self.deletekakko(answer + a, copi)
            i += 1
        return answer

    def kakko(self, arr):
        mae = 0
        ushiro = 0
        for i in arr:
            if i == "(":
                mae += 1
            else:
                ushiro += 1
            if mae < ushiro:
                return False
        return True

S = RemovingParenthesis()
arr = "((()()()))"

answer = S.countWays(arr)
print answer
