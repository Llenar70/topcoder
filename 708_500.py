# coding:utf-8


class BuildingStrings():

    def __init__(self):
        self = self

    def findAny(self, K):
        ret_list = []
        string = ""
        if K <= 50:
            for i in range(K):
                string = string + "a"
            ret_list.append(string)
        elif 50 < K < 1250:
            a_strs = K // 50
            amari = K % 50
            for i in range(a_strs):
                ret_list.append("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            for i in range(amari):
                string = string + "a"
            ret_list.append(string)
        else:
            a_strs = K // 1250
            amari = K % 1250
            for i in range(a_strs):
                ret_list.append("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy")
            gozyu_strs = amari // 50
            print gozyu_strs
            gozyu_amari = amari % 50
            if gozyu_strs != 0:
                for i in range(2):
                    for i in [chr(i) for i in range(97, 97 + gozyu_strs)]:
                        string = string + i
                while len(string) < 50:
                    string = string + "a"
                ret_list.append(string)
            string = ""
            if gozyu_amari != 0:
                for i in range(gozyu_amari):
                    string = string + "a"
                ret_list.append(string)
        return tuple(ret_list)

S = BuildingStrings()
answer = S.findAny(1)
print answer
