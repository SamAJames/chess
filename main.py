from boardClass import Board
from Player import Player


def changePlayer(turn):
    if turn % 2 == 0:
        return 0
    else:
        return 1


def main():
    players = [""]*2
    print(players)
    players[0] = Player("w")
    players[1] = Player("b")
    board = Board()
    board.printBoard()

    turn = 0
    gameOver = False
    currentPlayer = players[changePlayer(turn)]

    while not gameOver:
        # Take move
        if currentPlayer.player == "b":
            print(currentPlayer.name +"'s Turn")
        elif currentPlayer.player == "w":
            print(currentPlayer.name + "'s Turn")

        while True:
            currentPlayer.setMove()
            move = currentPlayer.getMove()
            words, legalMove = (board.movePiece(currentPlayer.player, move[0], move[1]))
            if legalMove:
                break
            else:
                print(words)

        board.printBoard()
        print(words)
        print("Previous Move: ", move)



        # Change turn
        turn += 1
        currentPlayer = players[changePlayer(turn)]




if __name__ == "__main__":
    main()
