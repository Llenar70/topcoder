# coding:utf-8


class RangeEncoding():

    def __init__(self):
        self = self

    def minRanges(self, arr):
        arr = list(arr)
        n = arr[0]
        if len(arr) == 1:
            return 1
        answer = 1
        for i in arr[1:]:
            if n + 1 != i:
                answer += 1
            n = i
        return answer

S = RangeEncoding()
arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

answer = S.minRanges(arr)
print answer
