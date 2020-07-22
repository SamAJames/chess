#pieceClass.py

class Piece:
    def __init__(self, colour):
        self.colour = colour
        
      
      
class Rook(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "R"
        self.moves = [[-8, 0], [-7, 0], [-6, 0], [-5, 0], [-4, 0], [-3, 0], [-2, 0], [-1, 0], 
                        [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], 
                        [0, -8], [0, -7], [0, -6], [0, -5], [0, -4], [0, -3], [0, -2], [0, -1], 
                        [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]]
        self.jump = False
        self.normalTake = True
        self.specialMove = False

class Knight(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "N"
        self.moves = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        self.jump = True
        self.normalTake = True
        self.specialMove = False

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "B"
        self.moves = [[-8, -8], [-7, -7], [-6, -6], [-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1],
                        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8],
                        [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], 
                        [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8]]
        self.jump = False
        self.normalTake = True
        self.specialMove = False

class Queen(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "Q"
        self.moves = [[-8, 0], [-7, 0], [-6, 0], [-5, 0], [-4, 0], [-3, 0], [-2, 0], [-1, 0], 
                        [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], 
                        [0, -8], [0, -7], [0, -6], [0, -5], [0, -4], [0, -3], [0, -2], [0, -1], 
                        [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], 
                        [-8, -8], [-7, -7], [-6, -6], [-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1],
                        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8],
                        [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], 
                        [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8]]
        self.jump = False
        self.normalTake = True
        self.specialMove = False

class King(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "K"
        self.moves = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        self.jump = False
        self.normalTake = True
        self.specialMove = True
        self.specialMoves = [[-3, 0], [2, 0]]
    
    def pieceMoved(self):
        self.specialMove = False
                      
class Pawn(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "P"
        self.moves = [[0, 1]]
        self.jump = False
        self.normalTake = False
        self.takes = [[-1, 1], [1, 1]]
        self.specialMove = True
        self.specialMoves = [[0, 2]]
    
    def pieceMoved(self):
        self.specialMove = False