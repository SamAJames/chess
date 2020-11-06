

def testBoard(generated, target, name):
    if generated == target:
        print("Passed " + name)
    else:
        print("Failed " + name)

def runTests(BoardClass):
    board = BoardClass()
    testBoard(board.getBoardShort(), "RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr", "Test 1 - basic board setup")
    
    board.movePiece('w', 'A2', 'A3')
    testBoard(board.getBoardShort(), "RNBQKBNR0PPPPPPPP0000000000000000000000000000000pppppppprnbqkbnr", "Test 2 - move pawn one space")
    
    board.movePiece('w', 'E2', 'E4')
    testBoard(board.getBoardShort(), "RNBQKBNR0PPP0PPPP00000000000P0000000000000000000pppppppprnbqkbnr", "Test 3 - move pawn two spaces")
    
    board.movePiece('w', 'B1', 'C3')
    testBoard(board.getBoardShort(), "R0BQKBNR0PPP0PPPP0N000000000P0000000000000000000pppppppprnbqkbnr", "Test 4 - knight jumps over piece")
    
    board.movePiece('w', 'D1', 'F3')
    testBoard(board.getBoardShort(), "R0B0KBNR0PPP0PPPP0N00Q000000P0000000000000000000pppppppprnbqkbnr", "Test 5 - move queen diagonally")
    
    board.movePiece('w', 'H1', 'H5')
    testBoard(board.getBoardShort(), "R0B0KBNR0PPP0PPPP0N00Q000000P0000000000000000000pppppppprnbqkbnr", "Test 6 - rook can't move through pieces")
    
    board.movePiece('b', 'D7', 'D5')
    testBoard(board.getBoardShort(), "R0B0KBNR0PPP0PPPP0N00Q000000P000000p000000000000ppp0pppprnbqkbnr", "Test 7 - move black pawn")
    
    board.movePiece('w', 'E4', 'D5')
    testBoard(board.getBoardShort(), "R0B0KBNR0PPP0PPPP0N00Q0000000000000P000000000000ppp0pppprnbqkbnr", "Test 8 - pawn takes diagonally")
