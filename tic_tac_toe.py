# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

board = [" " for n in range(9)]

# Function for displaying the board
def displayBoard(board: list):
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

# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    displayBoard(board)

