# coding:utf-8


class StepsConstruct():

    def __init__(self):
        self = self

    def construct(self, board, k):
        board = list(board)
        if board[0][0] == "#":
            return ""
        elif board[-1][-1] == "#":
            return ""
        print len(board)
        print len(board[0])
        now_stay = [0, 0]
        n = 0
        routes = [""]
        while n < k:
            if now_stay == [len(board) - 1, len(board[0]) - 1]:
                break

            if now_stay[1] + 1 <= len(board[0]) - 1:
                if board[now_stay[0]][now_stay[1] + 1] == "." and routes[-1] != "LRL":
                    n = n + 1
                    now_stay[1] = now_stay[1] + 1
                    routes.append("R")
                    print now_stay
                    print routes
                if now_stay[0] + 1 <= len(board) - 1 and n < k:
                    if board[now_stay[0] + 1][now_stay[1]] == "." and routes[-1] != "UDU":
                        n = n + 1
                        now_stay[0] = now_stay[0] + 1
                        routes.append("D")
                        print now_stay
                        print routes
                        continue

            if now_stay[0] + 1 <= len(board) - 1:
                if board[now_stay[0] + 1][now_stay[1]] == "." and routes[-1] != "UDU":
                    n = n + 1
                    now_stay[0] = now_stay[0] + 1
                    routes.append("D")
                    print now_stay
                    print routes
                    continue
            if now_stay[0] - 1 >= 0:
                if board[now_stay[0] - 1][now_stay[1]] == "." and routes[-1] != "DUD":
                    n = n + 1
                    now_stay[0] = now_stay[0] - 1
                    routes.append("U")
                    print now_stay
                    print routes
                    continue
            if now_stay[1] - 1 >= 0:
                if board[now_stay[0]][now_stay[1] - 1] == "." and routes[-1] != "RLR":
                    n = n + 1
                    now_stay[1] = now_stay[1] - 1
                    routes.append("L")
                    print now_stay
                    print routes
                    continue
            return ""
        print routes
        print now_stay
        print len(board)

        if now_stay == [len(board) - 1, len(board[0]) - 1]:
            if n == k:
                return "".join(routes)
            else:
                if (k - n) % 2 == 0:
                    if routes[-1] == "D":
                        while n < k:
                            routes.append("UD")
                            n = n + 2
                    if routes[-1] == "R":
                        while n < k:
                            routes.append("LR")
                            n = n + 2
                    return "".join(routes)
                return ""
        return ""


S = StepsConstruct()
b = ("...",
     ".#.",
     "...")
k = 4
b = ("...",
     ".#.",
     "...")
k = 12
b = ("...#.",
     "..#..",
     ".#...")
k = 100
# b = ("..#",
#      "#.#",
#      "..#",
#      ".#.",
#      "...")
# k = 6
# b = (".#...",
#      ".#.#.",
#      ".#.#.",
#      ".#.#.",
#      "...#.")
# k = 16
# b = ("#.",
#      "..")
# k = 2
b = (".#...",
     ".#.#.",
     ".#.#.",
     ".#.#.",
     "...#.")
k = 2999
b = ("..#........",
     "...#.......",
     ".#.........",
     "........#..",
     ".#.........",
     "...........",
     "...##......",
     ".#..#.....#",
     "........#..",
     ".#.....#...",
     "..#.......#",
     ".....#....#",
     ".#.....#...",
     "..........#",
     "...........",
     "...........",
     "...##......",
     "...........",
     ".....#..#..",
     "..#......#.",
     ".........#.",
     "...........",
     "...........",
     "...........",
     ".........#.",
     ".#........#",
     "...........",
     "...........",
     "...........",
     "...........",
     "...........",
     "...........",
     "...#.......",
     "..#........",
     "..........#",
     ".#......#..",
     "..........#",
     "...#.......",
     "..#........",
     ".......#...",
     "........#..")
k = 210


answer = S.construct(b, k)
print answer
