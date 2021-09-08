import numpy as np

class GameState():
    def __init__(self):
        self.board = np.array(
           [
               ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
               ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
               ["--", "--", "--","--", "--", "--", "--", "--",],
               ["--", "--", "--","--", "--", "--", "--", "--",],
               ["--", "--", "--","--", "--", "--", "--", "--",],
               ["--", "--", "--","--", "--", "--", "--", "--",],
               ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
               ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
           ]
       )
        self.whiteToMove = True
        self.moveLog = []
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

class Move():
    # maps keys to values
    # key: value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"A": 0, "B": 1, "C": 2, "D": 3,
                   "E": 4, "F": 5, "G": 6, "H": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startPos, endPos, board):
        self.startRow = startPos[0]
        self.startCol = startPos[1]
        self.endRow = endPos[0]
        self.endCol = endPos[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + " " + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]



