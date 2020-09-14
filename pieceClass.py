#pieceClass.py

class Piece:
    def __init__(self, colour):
        self.colour = colour
        self.jump = False
        self.normalTake = True
        self.specialMove = False
        
    def symbol(self, piece, colour):
        if colour == 'b':
            piece = piece.lower()
        return piece
      
      
class Rook(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = super().symbol("R", colour)
        self.moves = [[-8, 0], [-7, 0], [-6, 0], [-5, 0], [-4, 0], [-3, 0], [-2, 0], [-1, 0], 
                        [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], 
                        [0, -8], [0, -7], [0, -6], [0, -5], [0, -4], [0, -3], [0, -2], [0, -1], 
                        [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]]


class Knight(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = super().symbol("N", colour)
        self.moves = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        self.jump = True


class Bishop(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = super().symbol("B", colour)
        self.moves = [[-8, -8], [-7, -7], [-6, -6], [-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1],
                        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8],
                        [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], 
                        [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8]]


class Queen(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = super().symbol("Q", colour)
        self.moves = [[-8, 0], [-7, 0], [-6, 0], [-5, 0], [-4, 0], [-3, 0], [-2, 0], [-1, 0], 
                        [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], 
                        [0, -8], [0, -7], [0, -6], [0, -5], [0, -4], [0, -3], [0, -2], [0, -1], 
                        [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], 
                        [-8, -8], [-7, -7], [-6, -6], [-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1],
                        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8],
                        [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], 
                        [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8]]


class King(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = super().symbol("K", colour)
        self.moves = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        self.specialMove = True
        self.specialMoves = [[-3, 0], [2, 0]]
    
    def pieceMoved(self):
        self.specialMove = False
                      
class Pawn(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = super().symbol("P", colour)
        
        if colour == 'w':
            direction = 1
        elif colour == 'b':
            direction = -1
            
        self.moves = [[0, direction]]
        self.normalTake = False
        self.takes = [[-1, direction], [1, direction]]
        self.specialMove = True
        self.specialMoves = [[0, 2*direction]]
    
    def pieceMoved(self):
        self.specialMove = False