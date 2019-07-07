# coding:utf-8


class MakePalindrome():

    def __init__(self):
        self = self

    def constructMinimal(self, card):
        pair_list = []
        card_list = list(card)
        for i in range(len(card)):
            str1 = list(card)[i]
            for s in list(card)[i + 1:]:
                if str1 == s:
                    # str1 count2?
                    count = 0
                    for c in list(card_list):
                        if str1 == c:
                            count = count + 1
                        if count >= 2:
                            card_list.remove(str1)
                            card_list.remove(str1)
                            pair_list.append(str1)
                            break
        pal = ""
        pal_list = []
        for s in pair_list:
            pal = pal + s

        if len(card_list) != 0:
            pal = pal + card_list[0]
            card_list.pop(0)

        pair_list.reverse()
        for s in pair_list:
            pal = pal + s
        pal_list.append(pal)
        pal_list.extend(card_list)
        return tuple(pal_list)


S = MakePalindrome()
card = "dasudiahoidsakldnalubdlisauhdjaklndsaldbasuidhaklnxaalnxalsuldhauflndjclkusaildusaijnxaulisauasdnjsakudilasjdkandasuildjaknduasildjkasndasuldjkjansjdulisfudankdasludiaskljfnjsakdnasuilkfjandjasduliasduiaskdnaslufh;asdk;akdnasjkfbus;lsabduadnkandiagukhajdneksuvdknxalaiwlndlnawkjbfukcnajsdkajsdasbiudnasdlaoudahioncqwiemiquxrniufhojklssdxmijoqwuergteiumzqwkenxmtuhmiuzejxkqjriehrumqeiqwdj,xqhueoeicwqnruhqimhqwicuqhmireuhi,xkojhmweiutchumjejdiohruwiehlskjfddjklgutilwefjsdkfnjwurdfsnxzlcmmbvcxxcbaufhawoincdkzfnjabofskacndjgsihdocijlkasnmdlsancjndcuogiaodkascnudgobiaosdawmnduosgfaoskngoeianckanfdoahsiodasoknfeoighoishadokn,ldmdgbjoeorhaudasl;jp:r:aolmca.gbiehoa;g;klng;agaikvdlnl.nkvc;vi;iho;aweglhkvnmda/pwpeotj/adgkm/acs,c/asegs/ihnslnvmsl.asknfsdlgaiocklackld"
print S.constructMinimal(card)
