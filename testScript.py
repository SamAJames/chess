

def testBoard(generated, target, name):
    if generated == target:
        print("Passed " + name)
    else:
        print("Failed " + name)

def runTests(BoardClass):
    board = BoardClass()
    testBoard(board.getBoardShort(), "wRwNwBwQwKwBwNwRwPwPwPwPwPwPwPwP00000000000000000000000000000000bPbPbPbPbPbPbPbPbRbNbBbQbKbBbNbR", "Test 1 - basic board setup")
    
    board.movePiece('w', 'A2', 'A3')
    testBoard(board.getBoardShort(), "wRwNwBwQwKwBwNwR0wPwPwPwPwPwPwPwP0000000000000000000000000000000bPbPbPbPbPbPbPbPbRbNbBbQbKbBbNbR", "Test 2 - move pawn one space")
    
    board.movePiece('w', 'E2', 'E4')
    testBoard(board.getBoardShort(), "wRwNwBwQwKwBwNwR0wPwPwP0wPwPwPwP00000000000wP0000000000000000000bPbPbPbPbPbPbPbPbRbNbBbQbKbBbNbR", "Test 3 - move pawn two spaces")
    
    board.movePiece('w', 'B1', 'C3')
    testBoard(board.getBoardShort(), "wR0wBwQwKwBwNwR0wPwPwP0wPwPwPwP0wN000000000wP0000000000000000000bPbPbPbPbPbPbPbPbRbNbBbQbKbBbNbR", "Test 4 - knight jumps over piece")
    
    board.movePiece('w', 'D1', 'F3')
    testBoard(board.getBoardShort(), "wR0wB0wKwBwNwR0wPwPwP0wPwPwPwP0wN00wQ000000wP0000000000000000000bPbPbPbPbPbPbPbPbRbNbBbQbKbBbNbR", "Test 5 - move queen diagonally")
    
    board.movePiece('w', 'H1', 'H5')
    testBoard(board.getBoardShort(), "wR0wB0wKwBwNwR0wPwPwP0wPwPwPwP0wN00wQ000000wP0000000000000000000bPbPbPbPbPbPbPbPbRbNbBbQbKbBbNbR", "Test 6 - rook can't move through pieces")
    
    board.movePiece('b', 'D7', 'D5')
    testBoard(board.getBoardShort(), "wR0wB0wKwBwNwR0wPwPwP0wPwPwPwP0wN00wQ000000wP000000bP000000000000bPbPbP0bPbPbPbPbRbNbBbQbKbBbNbR", "Test 7 - move black pawn")
    
    board.movePiece('w', 'E4', 'D5')
    testBoard(board.getBoardShort(), "wR0wB0wKwBwNwR0wPwPwP0wPwPwPwP0wN00wQ0000000000000wP000000000000bPbPbP0bPbPbPbPbRbNbBbQbKbBbNbR", "Test 8 - pawn diagonal take")
    
    