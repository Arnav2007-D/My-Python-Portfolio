print("WELCOME TO ARNAV'S TICTACTOE GAME")
print("-------😄--------😄---------😄---")
print("\n")
board = [ "-", "-", "-",
          "-", "-", "-",
          "-", "-", "-" ]
current_player = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])   
#take player input
def playerInput(board):
    global current_player
    while True:
        inp = input("Enter a number 1-9: ")
        try:
            inp = int(inp)
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        if 1 <= inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = current_player
            break
        else:
            print("Invalid move (out of range or spot taken). Try again!")
            print("---🥴-----🥴-----🥴-----🥴--")



def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[1]
        return True 
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[7]
        return True 
def checkRow(board):
    global winner 
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-": 
        winner = board[5]
        return True
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("GAME TIE!")
        print("😊-----😊")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}")
        print("-🥳----🥳-----🥳-----🥳")
        gameRunning = False
              
def switchPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"




while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    if gameRunning:
        switchPlayer()

