# NOT WORKING?
import numpy as np
# READ FILE
with open('test.txt') as f:
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
    print("CALC DRAWNNUMBERS {}".format(drawnNumbers))
    notDrawnNumbers = []
    for row in board:
        notDrawnNumbers = notDrawnNumbers + \
            [number for number in row if number not in drawnNumbers]
    return sum(notDrawnNumbers)


def checkHorizonalWin(boards, drawnNumbers):
    print("chekH DRAWNNUMBERS {}".format(drawnNumbers))
    isWin = False
    score = 0
    winningBoard = 0
    for boardNumber, board in enumerate(boards):
        for rowNumber in range(boardMaxRows):
            if set(board[rowNumber]).issubset(drawnNumbers):
                isWin = True
                winningBoard = boardNumber
                score = calculateScore(board, drawnNumbers)
    return isWin, score, winningBoard


def checkVerticalWin(boards, drawnNumbers):
    print("chekV DRAWNNUMBERS {}".format(drawnNumbers))
    isWin = False
    score = 0
    winningBoard = 0
    for boardNumber, board in enumerate(boards):
        board = np.array(board).transpose()
        for rowNumber in range(boardMaxRows):
            if set(board[rowNumber]).issubset(drawnNumbers):
                isWin = True
                winningBoard = boardNumber
                score = calculateScore(board, drawnNumbers)
    return isWin, score, winningBoard


# THE LOOP
alreadyWonBoards = []
for theNumberThatWasJustCalled in randomNumbers:
    drawnNumbers.append(theNumberThatWasJustCalled)
    print("DRAWNNUMBERS {}".format(drawnNumbers))

    hWin, hScore, hWinningBoard = checkHorizonalWin(boards, drawnNumbers)
    if hWin and hWinningBoard not in alreadyWonBoards:
        print("We have a winner with Number {} and the Score {} with Board {}".format(
            theNumberThatWasJustCalled, hScore*theNumberThatWasJustCalled, hWinningBoard))
        alreadyWonBoards.append(hWinningBoard)

    vWin, vScore, vWinningBoard = checkVerticalWin(boards, drawnNumbers)
    if vWin and vWinningBoard not in alreadyWonBoards:
        print("We have a winner with Number {} and the Score {} with Board {}".format(
            theNumberThatWasJustCalled, vScore*theNumberThatWasJustCalled, vWinningBoard))
        alreadyWonBoards.append(vWinningBoard)
