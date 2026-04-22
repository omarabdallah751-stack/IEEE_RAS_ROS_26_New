while True:
    symbol = input("Please Choose one of X or O: ").upper()
    if symbol == "O":
        print(f"First Player you have Choosen: {symbol}")
        break  
    elif symbol == "X":
        print(f"First Player you have Choosen: {symbol}")
        break  
    else:
        print("you didn't choose anyone of them please choose again")

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def check_winner(board):
    if board[0][0]==board[1][1]==board[2][2] and board[0][0] != " ":
        return board[0][0]
    elif board[0][2]==board[2][2]==board[2][0] and board[0][2] != " ":
        return board[0][2]
    for row in board:    
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]    
    return None   


current_symbol = symbol 
turns = 0


while turns < 9:
    
    row_input = int(input(f"Player {current_symbol}, choose a row (1-3): "))
    col_input = int(input(f"Player {current_symbol}, choose a column (1-3): "))
    
    row = row_input - 1
    col = col_input - 1
    
    if board[row][col] == " ":
       board[row][col] = current_symbol
       turns += 1

       print("\nCurrent Board:")
       print(board[0])
       print(board[1])
       print(board[2])

       if current_symbol == "X":
           current_symbol = "O" 
       else:
           current_symbol = "X"

    else:
        print("The place is taken Choose another place")



    winner = check_winner(board)
    if winner != None:
        print(f"Congratulation player {winner}")
        break

    x = 0
    y = 0
    is_full = True
    while x < 3:
        if board[x][y] == " ":
            is_full = False
            break
        y += 1
        if y == 3:
            y = 0
            x += 1    
            
    if is_full:
        print("The board is completely full")
        print("Draw >_<")
        break
































