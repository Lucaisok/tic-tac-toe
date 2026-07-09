# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

board = [" " for n in range(9)]
# player_one_name = ""
# player_two_name = ""
# player_one_symbol = ""
# player_two_symbol = ""
# current_player = player_one_name
# current_symbol = player_one_symbol

def draw_board(board):
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

# Function for displaying the board
def displayBoard(board: list):
    draw_board(board)
    player_one_name = input("Hi, player one. What is your name?")
    player_two_name = input("Hi, player two. What is your name?") 
    print(player_one_name)
    print(player_two_name)
    player_one_symbol = input(f"Hi {player_one_name}, choose a symbol: 'X' or 'O'")
    player_two_symbol = input(f"Hi {player_two_name} player two, choose a symbol: 'X' or 'O'")
    print(f"Hi {player_one_name}, your symbol is {player_one_symbol}")
    print(f"Hi {player_two_name}, your symbol is {player_two_symbol}")

    current_player = player_one_name
    current_symbol = player_one_symbol

    for turn in range(9):
        print(f"Is {current_player}'s turn")
        picked_cell = input("pick your cell (1 - 9)")
        print(f"picked cell is {picked_cell}")
        index = int(picked_cell) -1
        board[index] = current_symbol
        draw_board(board)
        if current_player == player_one_name:
            current_player = player_two_name
            current_symbol = player_two_symbol
        else:
            current_player = player_one_name
            current_symbol = player_one_symbol

# def assign_players():
#     player_one_name = input("Hi, player one. What is your name?")
#     player_two_name = input("Hi, player two. What is your name?") 
#     print(player_one_name)
#     print(player_two_name)
#     player_one_symbol = input(f"Hi {player_one_name}, choose a symbol: 'X' or 'O'")
#     player_two_symbol = input(f"Hi {player_two_name} player two, choose a symbol: 'X' or 'O'")
#     print(f"Hi {player_one_name}, your symbol is {player_one_symbol}")
#     print(f"Hi {player_two_name}, your symbol is {player_two_symbol}")

# def pick_cell():
#      for turn in range(9):
#          print(f"Is {current_player}'s turn")
#          picked_cell = input("pick your cell (1 - 9)")
#          print(f"picked cell is {picked_cell}")
#          index = picked_cell -1
#          board[index] = current_symbol
#          if current_player == player_one_name:
#             current_player = player_two_name
#             current_symbol = player_two_symbol
#          else:
#              current_player = player_one_name
#              current_symbol = player_one_symbol
         
        
             



# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    displayBoard(board)
    # assign_players()
    # pick_cell()
    displayBoard(board)
    # print(current_player)
    # print(current_symbol)
    