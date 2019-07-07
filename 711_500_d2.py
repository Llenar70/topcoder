# coding:utf-8


class StringTransform():

    def __init__(self):
        self = self

    def isPossible(self, s, t):
        list_s = list(s)
        list_t = list(t)
        list_s.reverse()
        list_t.reverse()

        for str_s, str_t, i in zip(list_s, list_t, range(len(list_s))):
            if str_s != str_t:
                if str_t not in list_s[i + 1:]:
                    return "Impossible"
        return "Possible"

S = StringTransform()
s = "abc"
t = "aba"
answer = S.isPossible(s, t)
print answer
