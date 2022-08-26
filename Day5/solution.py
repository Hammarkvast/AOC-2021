board = [[0 for i in range(1000)] for j in range(1000)]

with open("input.txt") as f:
    for line in f:
        li = line.strip()
        lst = li.split("->")
        x1y1 = tuple(int(x) for x in lst[0].split(","))
        x2y2 = tuple(int(x) for x in lst[1].split(","))
        x1 = x1y1[0]
        x2 = x2y2[0]
        y1 = x1y1[1]
        y2 = x2y2[1]
        if x1 == x2 and y1 != y2:
            if y1 > y2:
                while y1 >= y2:
                    board[y1][x1]+=1
                    y1-=1
            elif y1 < y2:
                while y1 <= y2:
                    board[y1][x1]+=1
                    y1+=1
        elif y1 == y2 and x1 != x2:
            if x1 > x2:
                while x1 >= x2:
                    board[y1][x1]+=1
                    x1-=1
            elif x1 < x2:
                while x1 <= x2:
                    board[y1][x1]+=1
                    x1+=1
        elif x1 < x2 and y1 < y2:
            while x1 <= x2:
                board[y1][x1]+=1
                x1+=1
                y1+=1
        elif x1 < x2 and y1 > y2:
            while x1 <= x2:
                board[y1][x1]+=1
                x1+=1
                y1-=1
        elif x1 > x2 and y1 < y2:
            while x1 >= x2:
                board[y1][x1]+=1
                x1-=1
                y1+=1
        elif x1 > x2 and y1 > y2:
            while x1 >= x2:
                board[y1][x1]+=1
                x1-=1
                y1-=1

# x1 < x2 && y1 < y2
# x1 < x2 && y1 > y2
# x1 > x2 && y1 < y2
# x1 > x2 && y1 > y2


def testSolution():
    #print(board)
    crossings = 0
    for row in board:
        for num in row:
            if num > 1:
                crossings+=1
    print(crossings)

[[0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
[0, 1, 1, 2, 1, 1, 1, 2, 1, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[2, 2, 2, 1, 1, 1, 0, 0, 0, 0]]

testSolution()