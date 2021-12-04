bingoBoards = []
board = []
draws = []
with open("input.txt") as f:
    for line in f:
        if line == "\n":
            bingoBoards.append(board)
            board = []
            continue
        numbers = line.split()
        row = {}
        for number in numbers:
            row[int(number)] = False
        board.append(row)

with open("draws.txt") as f:
    for line in f:
        lst = line.split(',')
        for num in lst:
            draws.append(int(num))

#PART 1

def gameLoop(boards, bingoDraws):
    for draw in bingoDraws:
        for board in boards:
            markBoard(board, draw)
            vert = checkVertical(board)
            hori = checkHorizontal(board)
            if vert:
                return vert * draw
            elif hori:
                return hori * draw
        # win = checkWinner(boards, draw)
        # if win:
        #     return win

def markBoard(board, draw):
    for row in board:
        for (num, _) in row.items():
            if num == draw:
                row[num] = True
                return

def checkVertical(board):
    matrix, truthmatrix, winningCol = [], [], []
    for row in board:
        matrix.append(list(row.keys()))
        truthmatrix.append(list(row.values()))
    cols, rows = 5, 5
    for j in range(cols):
        winningCol = []
        for i in range(rows):
            if truthmatrix[i][j]:
                winningCol.append(matrix[i][j])
            if len(winningCol) == 5:
                return countUnmarked(board)

def checkHorizontal(board):
    for row in board:
        winningRow = []
        for (num, marked) in row.items():
            if marked:
                winningRow.append(num)
        if len(winningRow) == 5:
            unmarkedNumbers = countUnmarked(board)
            return unmarkedNumbers
        

def countUnmarked(board):
    unmarked = []
    for row in board:
        for (num, marked) in row.items():
            if not marked:
                unmarked.append(num)
    return sum(unmarked)

#PART 2

def gameLoop2(boards, draws):
    winners = []
    winningBoard = []
    for draw in draws:
        for board in boards:
            markBoard(board, draw)
            vert = checkVertical(board)
            hori = checkHorizontal(board)
            if vert and board not in winningBoard:
                winningBoard.append(board)
                winners.append((vert, draw))
            elif hori and board not in winningBoard:
                winningBoard.append(board)
                winners.append((hori, draw))
    return winners[-1][0] * winners[-1][1]

#testDraws = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
#testBoards = [[{22: False, 13: False, 17: False, 11: False, 0: False}, {8: False, 2: False, 23: False, 4: False, 24: False}, {21: False, 9: False, 14: False, 16: False, 7: False}, {6: False, 10: False, 3: False, 18: False, 5: False}, {1: False, 12: False, 20: False, 15: False, 19: False}],
#           [{3: False, 15: False, 0: False, 2: False, 22: False}, {9: False, 18: False, 13: False, 17: False, 5: False}, {19: False, 8: False, 7: False, 25: False, 23: False}, {20: False, 11: False, 10: False, 24: False, 4: False}, {14: False, 21: False, 16: False, 12: False, 6: False}], 
#           [{14: False, 21: False, 17: False, 24: False, 4: False}, {10: False, 16: False, 15: False, 9: False, 19: False}, {18: False, 8: False, 23: False, 26: False, 20: False}, {22: False, 11: False, 13: False, 6: False, 5: False}, {2: False, 0: False, 12: False, 3: False, 7: False}]]

print(f"Solution part 1: {gameLoop(bingoBoards, draws)}")
print(f"Solution part 2: {gameLoop2(bingoBoards, draws)}")