# Run `uv run python tic_tac_toe.py` in the command line to start the game

def display_board(board):
    display = []
    for i in range(9):
        if board[i] == " ":
            display.append(str(i + 1))  # show the number if empty
        else:
            display.append(board[i])    # show X or O if filled
    
    print(display[0] + " | " + display[1] + " | " + display[2])
    print("---------")
    print(display[3] + " | " + display[4] + " | " + display[5])
    print("---------")
    print(display[6] + " | " + display[7] + " | " + display[8])

def assign_players():
    player_one_name = input("Hi, player one. What is your name?")
    player_two_name = input("Hi, player two. What is your name?") 
    print(player_one_name)
    print(player_two_name)
    player_one_symbol = input(f"Hi {player_one_name}, choose a symbol: 'X' or 'O'")
    player_two_symbol = input(f"Hi {player_two_name} player two, choose a symbol: 'X' or 'O'")
    print(f"Hi {player_one_name}, your symbol is {player_one_symbol}")
    print(f"Hi {player_two_name}, your symbol is {player_two_symbol}")
    return player_one_name, player_two_name, player_one_symbol, player_two_symbol

def check_winner(board):
    winning_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for combo in winning_combos:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != " ":
            return True  

    return False  # no winner yet

def check_draw(board):
   if " " not in board:
       return True
   else:
       return False
   
def game(board, player_one_name, player_two_name, player_one_symbol, player_two_symbol, current_player, current_symbol):
    for turn in range(9):
        print(f"Is {current_player}'s turn")
        picked_cell = input("pick your cell (1 - 9)")
        print(f"picked cell is {picked_cell}")
        index = int(picked_cell) -1
        if board[index] == " ":
            board[index] = current_symbol
            display_board(board)
            win = check_winner(board)
            if win:
                print(f"winner is {current_player}")
                break
            draw = check_draw(board)
            if draw:
                print("Draw!")
                break         
            if current_player == player_one_name:
                current_player = player_two_name
                current_symbol = player_two_symbol
            else:
                current_player = player_one_name
                current_symbol = player_one_symbol
        else:
            print("cell already taken, please pick again")
            display_board(board)

def play():
    board = [" " for n in range(9)]
    player_one_name, player_two_name, player_one_symbol, player_two_symbol = assign_players()
    current_player = player_one_name
    current_symbol = player_one_symbol
    display_board(board)
    game(board, player_one_name, player_two_name, player_one_symbol, player_two_symbol, current_player, current_symbol)


# Tic-tac-toe game
if __name__ == "__main__":
    print("Welcome to a new round of Tic-Tac-Toe!")
    play()

    