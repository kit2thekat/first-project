# This function defines my variables.

def main():
    introduction = intro()
    board = create_board()
    fancy = fancyboard(board)
    symbol_1, symbol_2 = symb()
    nospots = isfull(board, symbol_1, symbol_2)

# This function prints the introduction to the user.
    
def intro():
    
    print(''' Hey! Welcome to your Tik-Tak-Toe game!
          
    * Tic-tac-toe is played by two players, who choose where to place the marks X and O in one of the nine spaces in the grid.
    * Player one will be marked as X.
    * Player two will be marked as 0.
    * The board has 9 blocks. To make a move each player must select the block number by choosing any number between 1 and 9 (inclusive).''')
    

def create_board():

# This function creates a blank playboard
    
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board

def symb():
# This function decides the players symbols they want to use (X and O).
    symbol_1 = input("Hello player 1, would you like to be X or O? ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Player 2, you will be O this game!")
    else:
        symbol_2 = "X"
        print("Player 2, you will be X this game! ")
    input("Press enter to continue to the game!")
    print("\n")
    return(symbol_1, symbol_2)

def letsplay(board, symbol_1, symbol_2, count):
# This function starts the game.

    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Player " + player + ", it is your turn now. ")
    row = int(input("Pick a row: upper row: enter 0, middle row: enter 1, bottom row: enter 2 "))
    column = int(input("Pick a column: Left column: enter 0, middle column: enter 1, right column: enter 2 "))

    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outofrange(row, column)
        row = int(input("pick a row, upper row: enter 0, middle row: enter 1, bottom row: enter 2 "))
        column = int(input("Pick a column, left column: enter 0, middle column: enter 1, right column: enter 2 "))

    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        filled = wrongplace(board, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row upper row, enter 0, middle row: enter 1, bottom row: enter 2 "))
        column = int(input("Pick a column, left column: enter 0, middle column: enter 1, right column enter 2 ")) 
        
    if player == symbol_1:
        board[row][column] = symbol_1

    else:
        board[row][column] = symbol_2

    return (board)

def isfull(board, symbol_1, symbol_2):
    count = 1
    winner = True
# This function tests to see if the board is full.
    while count < 10 and winner == True:
        tryhard = letsplay(board, symbol_1, symbol_2, count)
        fancy = fancyboard(board)

        if count == 9:
            print(" The board is full. The game has now ended!")
            if winner == True:
                print("There is a tie! Congratulations!")
                
# Check if there is a winner.
        winner = winnertoday(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print(" Aww man Game is over :( ! )")

    report(count, winner, symbol_1, symbol_2)

def outofrange(row, column):
    print(" Sorry that choice is out of the boarder, pick another one. ")

def fancyboard(board):
# This function prints the board!
    rows = len(board)
    cols = len(board)
    print("---*------*---")
    for r in range(rows):
        print(board[r][0], " | ", board[r][1], " | ", board[r][2])
        print("---*------*---")
    return board

def winnertoday(board, symbol_1, symbol_2, count):
# This function checks if there is any winner yet.
    winner = True
    # Check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    # Check the diagnoal positions.
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Player " + symbol_1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    return winner

def wrongplace(board, symbol_1, symbol_2, row, column):
     print(" The square choice you have chosen was already picked, choose another spot! ")
     
def report(count,winner,symbol_1, symbol_2):
    print("\n")
    input("Press enter to see the game summary ")
    if (winner == False) and (count % 2 == 1 ):
        print("Winner : Player " + symbol_1 + ",")
    elif (winner == False) and (count % 2 == 0 ):
        print("Winner : Player " + symbol_2 + ",")
    else:
        print("There is a tie. ")

main()
