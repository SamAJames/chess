#boardClass.py
from pieceClass import*

import numpy as np

class Board:
    def __init__(self):
    
        # Setup pieces and the board in the classic format
        bR1 = Rook('b')
        bN1 = Knight('b')
        bB1 = Bishop('b')
        bQ1 = Queen('b')
        bK1 = King('b')
        bB2 = Bishop('b')
        bN2 = Knight('b')
        bR2 = Rook('b')
        bP1 = Pawn('b')
        bP2 = Pawn('b')
        bP3 = Pawn('b')
        bP4 = Pawn('b')
        bP5 = Pawn('b')
        bP6 = Pawn('b')
        bP7 = Pawn('b')
        bP8 = Pawn('b')
        wR1 = Rook('w')
        wN1 = Knight('w')
        wB1 = Bishop('w')
        wQ1 = Queen('w')
        wK1 = King('w')
        wB2 = Bishop('w')
        wN2 = Knight('w')
        wR2 = Rook('w')
        wP1 = Pawn('w')
        wP2 = Pawn('w')
        wP3 = Pawn('w')
        wP4 = Pawn('w')
        wP5 = Pawn('w')
        wP6 = Pawn('w')
        wP7 = Pawn('w')
        wP8 = Pawn('w')
        self.board = [[wR1, wP1, 0, 0, 0, 0, bP1, bR1],
                        [wN1, wP2, 0, 0, 0, 0, bP2, bN1], 
                        [wB1, wP3, 0, 0, 0, 0, bP3, bB1], 
                        [wQ1, wP4, 0, 0, 0, 0, bP4, bQ1], 
                        [wK1, wP5, 0, 0, 0, 0, bP5, bK1], 
                        [wB2, wP6, 0, 0, 0, 0, bP6, bB2], 
                        [wN2, wP7, 0, 0, 0, 0, bP7, bN2], 
                        [wR2, wP8, 0, 0, 0, 0, bP8, bR2]]

    def column(self, square):
        columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return columns[square[0]]
        
    def row(self, square):
        return int(square[1])-1 
                        
    def getBoardState(self):
        return self.board
        
    def setBoardState(self, newBoard):
        self.board = newBoard
        
    def movePiece(self, playerColour, startSquare, endSquare):
        if(self.checkValidPiece(playerColour, startSquare)):
            if(self.checkValidMove(playerColour, startSquare, endSquare)):
                newBoard = self.board
                newBoard[self.column(endSquare)][self.row(endSquare)] = self.board[self.column(startSquare)][self.row(startSquare)]
                newBoard[self.column(startSquare)][self.row(startSquare)] = 0
                self.setBoardState(newBoard)
                return "Move made"
            else:
                return "Not a valid move"
        else:
            return "Not a valid Piece"
    
    def checkValidPiece(self, playerColour, square):
    
        # Checks that the square chosen has a piece in it and that the colour of the piece matches that of the player
        if self.board[self.column(square)][self.row(square)] != 0:
            if self.board[self.column(square)][self.row(square)].colour == playerColour:
                return 1
        return 0
        
    def checkValidMove(self, playerColour, startSquare, endSquare):
    
        # Checks that the end square is on the board
        if self.column(endSquare) >= 0 and self.column(endSquare) <=7 and self.row(endSquare) >= 0 and self.row(endSquare) <= 7:
            move = [self.column(endSquare) - self.column(startSquare), self.row(endSquare) - self.row(startSquare)]
            piece = self.board[self.column(startSquare)][self.row(startSquare)]
            
            # Checks the chosen piece can reach the end square
            if move in piece.moves:
                if self.board[self.column(endSquare)][self.row(endSquare)] != 0:
                    if not piece.normalTake or piece.colour == self.board[self.column(endSquare)][self.row(endSquare)].colour:
                        return 0
                return self.checkClearPath(piece, move, startSquare, endSquare)
            
            # Checks if the move is a valid taking move (for a pawn only being able to take diagonally)
            if not piece.normalTake:
                if move in piece.takes and self.board[self.column(endSquare)][self.row(endSquare)] != 0:
                    if piece.colour == self.board[self.column(endSquare)][self.row(endSquare)].colour:
                        return 0
                    return 1
            
            # Checks if the move is a valis additional rule for specific pieces (pawn double forawrd or king castle)
            if piece.specialMove:
                if move in piece.specialMoves and self.board[self.column(endSquare)][self.row(endSquare)] == 0:
                    piece.pieceMoved()
                    return self.checkClearPath(piece, move, startSquare, endSquare)
        return 0
        
    def checkClearPath(self, piece, move, startSquare, endSquare):
    
        # Checks if any of the squares between the start and end square contain a piece
        if not piece.jump:
            for space in range(1, max(abs(np.array(move))), 1):
                if self.board[self.column(startSquare)+np.sign(move[0])*space][self.row(startSquare)+np.sign(move[1])*space] != 0:
                    return 0
        return 1
        
    def printBoard(self):
        for row in range(len(self.board[0])-1, -1, -1):
            for column in range(len(self.board)):
                symbol = str(self.board[column][row]) if isinstance(self.board[column][row], int) else self.board[column][row].symbol
                print(symbol, end = ' ')
            print()
        print()
    
    '''
    def checkCheck(self):
        
        
    def checkWin(self):
        
        
    def checkStalemate(self):   
        
        
    '''
        
    
'''  
game1 = Board()
game1.printBoard()
print(game1.movePiece('w', 'A2', 'A3'))
game1.printBoard()
print(game1.movePiece('w', 'E2', 'E4'))
game1.printBoard()
print(game1.movePiece('w', 'D1', 'F3'))
game1.printBoard()
print(game1.movePiece('w', 'F3', 'F7'))
game1.printBoard()
print(game1.movePiece('w', 'E4', 'E5'))
game1.printBoard()
print(game1.movePiece('w', 'E5', 'E6'))
game1.printBoard()
print(game1.movePiece('w', 'E6', 'E7'))
game1.printBoard()
print(game1.movePiece('w', 'E6', 'F7'))
game1.printBoard()
'''