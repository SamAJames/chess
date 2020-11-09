#boardClass.py
from pieceClass import*
from testScript import*

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
        return columns[square[0].upper()]
        
    def row(self, square):
        return int(square[1])-1 
                        
    def getBoardState(self):
        return self.board
        
    def getBoardShort(self):
        board = ''
        for column in range(len(self.board)):
            for row in range(len(self.board[0])):
                piece = self.board[row][column]
                if(piece == 0):
                    board = board + '0'
                else:
                    board = board + piece.symbol
        return board
        
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
            
            # Checks if the move is a valid additional rule for specific pieces (pawn double forward or king castle)
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
        print('  ', end = '')
        for i in range(65,73):
           print('  %c ' % i,  end='')
        print('\n  ', end='')
        print('+---'*8, end='+\n')
        for row in range(len(self.board[0])-1, -1, -1):
            print(row+1, end=' ')
            for column in range(len(self.board)):
                print('¦', end = ' ')
                symbol = str(self.board[column][row]) if isinstance(self.board[column][row], int) else self.board[column][row].symbol
                print(symbol, end = ' ')
            print('¦\n  +', end = '') 
            for column in range(len(self.board)):
                print('---+', end = '')
            print()
        print()

    def checkCheck(self):
        # Locate king
        # Look for adjacent pieces
        # Also check specifically for knights
        # If opponents pieces can take the king then check
        letter = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H"}
        for row in range(8):
            for col in range(8):
                if isinstance(self.board[col][row], King):
                    player = self.board[col][row].colour
                    check = False
                    kingPos = letter[col] + str(row+1)
                    diags = [self.diagonal, self.offDiagonal]
                    directions = [1, -1]
                    orthogonals = ["col", "row"]
                    # Check diagonals
                    for dir in directions:
                        for diag in diags:
                            rowCheck, colCheck, piece = self.checkDiagonal(row, col, dir, diag)
                            piecePos = letter[colCheck] + str(rowCheck+1)
                            try:
                                if piece.colour != player:
                                    check += self.checkValidMove(player, piecePos, kingPos)

                            except AttributeError:
                                # Occurs when nothing is returned. i.e. there is no piece in the position
                                pass

                        for axis in orthogonals:
                            rowCheck, colCheck, piece = self.checkOrthogonal(row, col, dir, axis)
                            piecePos = letter[colCheck] + str(rowCheck+1)
                            try:
                                if piece.colour != player:
                                    check += self.checkValidMove(player, piecePos, kingPos)

                            except AttributeError:
                                # Occurs when nothing is returned.
                                pass

                    if check:
                        if player == "b":
                            print("Lowercase", end="")
                        elif player == "w":
                            print("Caps", end="")
                        else:
                            pass

                        print(" king is in check.")


    def checkDiagonal(self, row, col, direction, diagonal):
        while True:
            row, col = diagonal(row, col, direction)
            if not (0 <= row < 8 and 0 <= col < 8):
                return 0, 0, 0
            if not isinstance(self.board[col][row], int):
                piece = self.board[col][row]
                return row, col, piece

    def checkOrthogonal(self, row, col, direction, constant):
        while True:
            if constant == "col":
                col += direction
            elif constant == "row":
                row += direction
            else:
                print("Should not happen")

            if not (0 <= row < 8 and 0 <= col < 8):
                return 0, 0, 0
            if not isinstance(self.board[col][row], int):
                piece = self.board[col][row]
                return row, col, piece

    def diagonal(self, row, col, direction):
        row += direction
        col += direction
        return row, col

    def offDiagonal(self, row, col, direction):
        row += direction
        col -= direction
        return row, col


    '''
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
# runTests(Board)