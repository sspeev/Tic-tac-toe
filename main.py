"""
Stoyan Peev XId class N22
This is the source code of the game tic tac toe
"""

import sys
import random
import os
import colorama
from colorama import Fore, Back
import time

def newBoard():
    """
	This function creates a nested list which we will use for the board of the game.
    """
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    return board

def printBoard(board):
    """
    Prints the board
    """
    for i in range(3):
        row = []
        for j in range(3):
            if board[i][j] == 0:
                row.append("  ")
            elif board[i][j] == 3:
                row.append("⭕")
            elif board[i][j] == 2:
                row.append("❌")
        print(Back.WHITE + (Fore.BLACK + "|" + Fore.RESET).join(row) + Back.RESET)

def makeMove(row, column, board):
    """
	This function receives the input of the player and the circle appers on the board
    """
    board[row-1][column-1] = 3
    return board

def validMove(row, column, board):
    """
	This function validate the player input
    """
    try:
        new_row = int(row)
        new_col = int(column)
        if 1 <= new_row <= 3 and 1 <= new_col <= 3:
            if board[new_row-1][new_col-1] == 0:
                return True
            else:
                print("Invalid input")
                return False
        else:
            print("Invalid input")
            return False
    except:
        print("Invalid input")
        return False

def vaildMoveComputer(row, column, board):
    try:
        if 0 <= row <= 2 and 0 <= column <= 2:
            if board[row][column] == 0:
                return True
            else:
                return False
        else:
            return False
    except:
        return False

def checkWinnerV(turn, board, nickname):
    """
    Checks is there a vertical win
    """
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != 0:
        if turn == 1:
            print(f" 🎉{nickname} won! Congratulations!🎉")
            return True
        elif turn == 2:
            print(f"{nickname}, you lost! Maybe next time...")
            return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != 0:
        if turn == 1:
            print(f"🎉{nickname} won! Congratulations!🎉")
            return True
        elif turn == 2:
            print(f"{nickname}, you lost! Maybe next time...")
            return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != 0:
        if turn == 1:
            print(f"🎉{nickname} won! Congratulations!🎉")
            return True
        elif turn == 2:
            print(f"{nickname}, you lost! Maybe next time...")
            return True
    else:
        return False

def checkWinnerH(turn, board, nickname):
    """
    Checks is there a horizontal win
    """
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != 0:
        if turn == 1:
            print(f"🎉{nickname} won! Congratulations!🎉")
            return True
        elif turn == 2:
            print(f"{nickname}, you lost! Maybe next time...")
            return True
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != 0:
        if turn == 1:
            print(f"🎉{nickname} won! Congratulations!🎉")
            return True
        elif turn == 2:
            print(f"{nickname}, you lost! Maybe next time...")
            return True
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != 0:
        if turn == 1:
            print(f"🎉{nickname} won! Congratulations!🎉")
            return True
        elif turn == 2:
            print(f"{nickname}, you lost! Maybe next time...")
            return True
    else:
        return False

def checkWinnerD(turn, board, nickname):
    """
    Checks is there a diagonal win
    """
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        if turn == 1:
            print(f"🎉{nickname} won! Congratulations!🎉")
            return True
        elif turn == 2:
            print(f"{nickname}, you lost! Maybe next time...")
            return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0:
        if turn == 1:
            print(f"🎉{nickname} won! Congratulations!🎉")
            return True
        elif turn == 2:
            print(f"{nickname}, you lost! Maybe next time...")
            return True
    else:
        return False

def checkWinner(turn, board, nickname):
    """
    Checks is there a winner
    """
    if checkWinnerV(turn, board, nickname) or checkWinnerH(turn, board, nickname) or checkWinnerD(turn, board, nickname):
        return True
    else:
        return False

def computerMove(board):
    """
	This function describes how the computer makes a move
    """
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while not vaildMoveComputer(row, col, board):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    board[row][col] = 2
    return board

def checkFull(board):
    '''
	Checks if the board is full
    '''
    counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                counter += 1
    if counter == 9:
        print("The game is a draw!")
        return True
    else:
        return False

def saveGame(filename, game):
    """
    Saves your game
    """
    try:
        with open(filename + ".txt", "x") as f:
            f.write(game["nickname"])
            f.write("\n")
            f.write(str(game["turn"]))
            f.write("\n")
            for row in game["board"]:
                f.write(" ".join([str(element) for element in row]))
                f.write("\n")
    except:
        print("Couldn’t save the game. Exiting now.")
    sys.exit()

def loadGame(filename):
    """
    Loads a saved game
    """
    while True:
        try:
            game = {}
            with open(filename + ".txt", "r") as f:
                game["nickname"] = f.readline().replace("\n","")
                game["turn"] = f.readline().replace("\n","")
                l1 = []
                line1 = [int(l) for l in f.readline().replace("\n","").split(" ")]
                l1.append(line1)
                line2 = [int(l) for l in f.readline().replace("\n","").split(" ")]
                l1.append(line2)
                line3 = [int(l) for l in f.readline().replace("\n","").split(" ")]
                l1.append(line3)
                game["board"] = l1
            return game
        except:
            print("File with that name hasn’t been found!")
            filename = input("Enter filename: ")

def startDesign(nickname):
    time.sleep(0.5)
    print(Fore.RED + nickname + Fore.RESET + " ")
    time.sleep(1.5)
    print(Fore.RED + "VS" + Fore.RESET)
    time.sleep(1.5)
    print(Fore.RED + "THE COMPUTER" + Fore.RESET + " ")

def Smart_comp(board):

    #Defence
    #VERTICAL
    #left
    if board[0][0] + board[1][0] == 6:
        if vaildMoveComputer(2, 0, board) == True:
            board[2][0] = 2
            return board
    if board[1][0] + board[2][0] == 6:
        if vaildMoveComputer(0, 0, board) == True:
            board[0][0] = 2
            return board
    if board[0][0] + board[2][0] == 6:
        if vaildMoveComputer(1, 0, board) == True:
            board[1][0] = 2
            return board

    #middle
    if board[0][1] + board[1][1] == 6:
        if vaildMoveComputer(2, 1, board) == True:
            board[2][1] = 2
            return board
    if board[1][1] + board[2][1] == 6:
        if vaildMoveComputer(0, 1, board) == True:
            board[0][1] = 2
            return board

    if board[0][1] + board[2][1] == 6:
        if vaildMoveComputer(1, 1, board) == True:
            board[1][1] = 2
            return board

    #right
    if board[0][2] + board[1][2] == 6:
        if vaildMoveComputer(2, 2, board) == True:
            board[2][2] = 2
            return board

    if board[1][2] + board[2][2] == 6:
        if vaildMoveComputer(0, 2, board) == True:
            board[0][2] = 2
            return board

    if board[0][2] + board[2][2] == 6:
        if vaildMoveComputer(1, 2, board) == True:
            board[1][2] = 2
            return board

    #HORIZONTAL
    #upper
    if board[0][0] + board[0][1] == 6:
        if vaildMoveComputer(0, 2, board) == True:
            board[0][2] = 2
            return board
    if board[0][1] + board[0][2] == 6:
        if vaildMoveComputer(0, 0, board) == True:
            board[0][0] = 2
            return board
    if board[0][0] + board[0][2] == 6:
        if vaildMoveComputer(0, 1, board) == True:
            board[0][1] = 2
            return board

    #middle
    if board[1][0] + board[1][1] == 6:
        if vaildMoveComputer(1, 2, board) == True:
            board[1][2] = 2
            return board
    if board[1][1] + board[1][2] == 6:
        if vaildMoveComputer(1, 0, board) == True:
            board[1][0] = 2
            return board

    if board[1][0] + board[1][2] == 6:
        if vaildMoveComputer(1, 1, board) == True:
            board[1][1] = 2
            return board

    #lower
    if board[2][0] + board[2][1] == 6:
        if vaildMoveComputer(2, 2, board) == True:
            board[2][2] = 2
            return board

    if board[2][1] + board[2][2] == 6:
        if vaildMoveComputer(0, 2, board) == True:
            board[2][0] = 2
            return board

    if board[2][0] + board[2][2] == 6:
        if vaildMoveComputer(2, 1, board) == True:
            board[2][1] = 2
            return board

     # left to right
    if board[0][0] + board[1][1] == 6:
        if vaildMoveComputer(2, 2, board) == True:
            board[2][2] = 2
            return board
    if board[1][1] + board[2][2] == 6:
        if vaildMoveComputer(0, 0, board) == True:
            board[0][0] = 2
            return board
    if board[0][0] + board[2][2] == 6:
        if vaildMoveComputer(1, 1, board) == True:
            board[1][1] = 2
            return board

    # right to left
    if board[0][2] + board[1][1] == 6:
        if vaildMoveComputer(2, 0, board) == True:
            board[2][0] = 2
            return board
    if board[1][1] + board[2][0] == 6:
        if vaildMoveComputer(0, 2, board) == True:
            board[0][2] = 2
            return board

    if board[0][2] + board[2][0] == 6:
        if vaildMoveComputer(1, 1, board) == True:
            board[1][1] = 2
            return board

        #Offence
        # VERTICAL
        # left
        if board[0][0] + board[1][0] == 4:
            if vaildMoveComputer(2, 0, board) == True:
                board[2][0] = 2
                return board
        if board[1][0] + board[2][0] == 4:
            if vaildMoveComputer(0, 0, board) == True:
                board[0][0] = 2
                return board
        if board[0][0] + board[2][0] == 4:
            if vaildMoveComputer(1, 0, board) == True:
                board[1][0] = 2
                return board

        # middle
        if board[0][1] + board[1][1] == 4:
            if vaildMoveComputer(2, 1, board) == True:
                board[2][1] = 2
                return board
        if board[1][1] + board[2][1] == 4:
            if vaildMoveComputer(0, 1, board) == True:
                board[0][1] = 2
                return board

        if board[0][1] + board[2][1] == 4:
            if vaildMoveComputer(1, 1, board) == True:
                board[1][1] = 2
                return board

        # right
        if board[0][2] + board[1][2] == 4:
            if vaildMoveComputer(2, 2, board) == True:
                board[2][2] = 2
                return board

        if board[1][2] + board[2][2] == 4:
            if vaildMoveComputer(0, 2, board) == True:
                board[0][2] = 2
                return board

        if board[0][2] + board[2][2] == 4:
            if vaildMoveComputer(1, 2, board) == True:
                board[1][2] = 2
                return board

        # HORIZONTAL
        # upper
        if board[0][0] + board[0][1] == 4:
            if vaildMoveComputer(0, 2, board) == True:
                board[0][2] = 2
                return board
        if board[0][1] + board[0][2] == 4:
            if vaildMoveComputer(0, 0, board) == True:
                board[0][0] = 2
                return board
        if board[0][0] + board[0][2] == 4:
            if vaildMoveComputer(0, 1, board) == True:
                board[0][1] = 2
                return board

        # middle
        if board[1][0] + board[1][1] == 4:
            if vaildMoveComputer(1, 2, board) == True:
                board[1][2] = 2
                return board
        if board[1][1] + board[1][2] == 4:
            if vaildMoveComputer(1, 0, board) == True:
                board[1][0] = 2
                return board

        if board[1][0] + board[1][2] == 4:
            if vaildMoveComputer(1, 1, board) == True:
                board[1][1] = 2
                return board

        # lower
        if board[2][0] + board[2][1] == 4:
            if vaildMoveComputer(2, 2, board) == True:
                board[2][2] = 2
                return board

        if board[2][1] + board[2][2] == 4:
            if vaildMoveComputer(0, 2, board) == True:
                board[2][0] = 2
                return board

        if board[2][0] + board[2][2] == 4:
            if vaildMoveComputer(2, 1, board) == True:
                board[2][1] = 2
                return board

        # left to right
        if board[0][0] + board[1][1] == 4:
            if vaildMoveComputer(2, 2, board) == True:
                board[2][2] = 2
                return board
        if board[1][1] + board[2][2] == 4:
            if vaildMoveComputer(0, 0, board) == True:
                board[0][0] = 2
                return board
        if board[0][0] + board[2][2] == 4:
            if vaildMoveComputer(1, 1, board) == True:
                board[1][1] = 2
                return board

        # right to left
        if board[0][2] + board[1][1] == 4:
            if vaildMoveComputer(2, 0, board) == True:
                board[2][0] = 2
                return board
        if board[1][1] + board[2][0] == 4:
            if vaildMoveComputer(0, 2, board) == True:
                board[0][2] = 2
                return board

        if board[0][2] + board[2][0] == 4:
            if vaildMoveComputer(1, 1, board) == True:
                board[1][1] = 2
                return board


    computerMove(board)

if __name__ == "__main__":
    board = newBoard()
    pl_input = input("🎮 Welcome to tic tac toe. Choose your option from the listed below: Press (n) ew game / (l) oad game 🎮: ")
    game = {"nickname": "", "turn": 0, "board": ""}
    while pl_input != 'n' and pl_input != 'l':
        pl_input = input("Press (n) ew game / (l) oad game: ")
    if pl_input == "n":
        nickname = input("Enter your nickname: ")
        game["nickname"] = nickname
        startDesign(nickname)
        time.sleep(0.5)
        print("To make a move, enter row and column numbers (from 1 to 3). To save the game, enter ‘s’ for a row.")
        print("Your turn")
        turn = 1
        game["turn"] = turn
        game["board"] = board
        #First Move of the game
        row = input("Enter row from 1 to 3: ")
        #saving
        if row == "s":
            filename = input("Enter filename: ")
            saveGame(filename, game)
        #saving
        col = input("Enter col from 1 to 3: ")
        while not validMove(row, col, board):
            row = input("Enter row from 1 to 3: ")
            # saving
            if row == "s":
                filename = input("Enter filename: ")
                saveGame(filename, game)
            # saving
            col = input("Enter col from 1 to 3: ")
        new_row = int(row)
        new_col = int(col)
        makeMove(new_row, new_col, board)
        printBoard(board)
        game["board"] = board
        #First Move of the game
        while True:
            print("Computer is thinking...")
            turn = 2
            game["turn"] = turn
            Smart_comp(board)
            time.sleep(2)
            printBoard(board)
            game["board"] = board
            if checkWinner(turn, board, nickname):
                break
            if checkFull(board):
                break

            print("Your turn")
            turn = 1
            game["turn"] = turn
            row = input("Enter row from 1 to 3: ")
            # saving
            if row == "s":
                filename = input("Enter filename: ")
                saveGame(filename, game)
            # saving
            col = input("Enter col from 1 to 3: ")
            while not validMove(row, col, board):
                row = input("Enter row from 1 to 3: ")
                # saving
                if row == "s":
                    filename = input("Enter filename: ")
                    saveGame(filename, game)
                # saving
                col = input("Enter col from 1 to 3: ")
            new_row = int(row)
            new_col = int(col)
            makeMove(new_row, new_col, board)
            printBoard(board)
            game["board"] = board
            if checkWinner(turn, board, nickname):
                break
            if checkFull(board):
                break

    elif pl_input == "l":
        filename = input("Enter file name: ")
        game = loadGame(filename)
        board = game["board"]
        turn = game["turn"]
        nickname = game["nickname"]
        os.remove(filename + ".txt")
        printBoard(board)

        while True:
            print("Your turn")
            turn = 1
            game["turn"] = str(turn)
            row = input("Enter row from 1 to 3: ")
            # saving
            if row == "s":
                filename = input("Enter filename: ")
                saveGame(filename, game)
            # saving
            col = input("Enter col from 1 to 3: ")
            while not validMove(row, col, board):
                row = input("Enter row from 1 to 3: ")
                # saving
                if row == "s":
                    filename = input("Enter filename: ")
                    saveGame(filename, game)
                # saving
                col = input("Enter col from 1 to 3: ")
            new_row = int(row)
            new_col = int(col)
            makeMove(new_row, new_col, board)
            printBoard(board)
            game["board"] = board
            if checkWinner(turn, board, nickname):
                break
            if checkFull(board):
                break

            print("Computer is thinking...")
            game["board"] = board
            turn = 2
            game["turn"] = str(turn)
            Smart_comp(board)
            time.sleep(2)
            printBoard(board)
            if checkWinner(turn, board, nickname):
                break
            if checkFull(board):
                break