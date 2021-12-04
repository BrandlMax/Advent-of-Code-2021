import numpy as np
# READ FILE
with open('input.txt') as f:
    input = f.read().splitlines()

# GET DRAW NUMBERS
randomNumbers = map(int, input[0].split(","))
drawnNumbers = []

# CLEAN DATA
del input[0:2]
rawBoards = list(filter(None, input))

# CREATE BOARDS
boardMaxRows = 5
currentBoard = 0
currentBoardRows = 1

amountBoards = len(rawBoards) / boardMaxRows
boards = [[] for _ in range(amountBoards)]

for idx, row in enumerate(rawBoards, start=1):
    row = map(int, list(filter(None, row.split(" "))))

    if currentBoardRows < boardMaxRows:
        boards[currentBoard].append(row)
        currentBoardRows = currentBoardRows + 1

    elif currentBoardRows == boardMaxRows:
        boards[currentBoard].append(row)
        # RESET
        if currentBoard < amountBoards - 1:
            currentBoard = currentBoard + 1
        currentBoardRows = 1


def calculateScore(board, drawnNumbers):
    notDrawnNumbers = []
    for row in board:
        notDrawnNumbers = notDrawnNumbers + \
            [number for number in row if number not in drawnNumbers]
    return sum(notDrawnNumbers)


def checkHorizonalWin(boards, drawnNumbers):
    isWin = False
    score = 0
    for board in boards:
        for rowNumber in range(boardMaxRows):
            if set(board[rowNumber]).issubset(drawnNumbers):
                isWin = True
                score = calculateScore(board, drawnNumbers)
    return isWin, score


def checkVerticalWin(boards, drawnNumbers):
    isWin = False
    score = 0
    for board in boards:
        board = np.array(board).transpose()
        for rowNumber in range(boardMaxRows):
            if set(board[rowNumber]).issubset(drawnNumbers):
                isWin = True
                score = calculateScore(board, drawnNumbers)
    return isWin, score


# THE LOOP
for theNumberThatWasJustCalled in randomNumbers:
    drawnNumbers.append(theNumberThatWasJustCalled)
    hWin, hScore = checkHorizonalWin(boards, drawnNumbers)
    vWin, vScore = checkVerticalWin(boards, drawnNumbers)
    if hWin:
        print("We have a winner with Number {} and the Score {}".format(
            theNumberThatWasJustCalled, theNumberThatWasJustCalled*hScore))
        break
    elif vWin:
        print("We have a winner with Number {} and the Score {}".format(
            theNumberThatWasJustCalled, theNumberThatWasJustCalled*vScore))
        break
