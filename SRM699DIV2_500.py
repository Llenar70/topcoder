# coding:utf-8


class LastDigit():

    def __init__(self):
        self = self

    def findX(self, S):
        low = 0
        high = S
        center = (low + high) / 2

        while (low <= high):
            if self.sum_all(center) == S:
                return center
            elif self.sum_all(center) < S:
                low = center + 1
            elif self.sum_all(center) > S:
                high = center - 1
            center = (low + high) / 2

        if self.sum_all(center) == S:
            return center
        else:
            return -1

    def sum_all(self, x):
        x_list = []
        for i in range(len(str(x))):
            if i == 0:
                x_list.append(x)
            else:
                x_list.append(str(x)[0:-i])
        x_sum = 0
        for j in x_list:
            x_sum = x_sum + int(j)
        return x_sum


last = LastDigit()
answer = last.findX(137174210616796)
print answer
