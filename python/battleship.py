'''
You can also add on to your Battleship! program to make it more 
complex and fun to play. Here are some ideas for enhancements — 
maybe you can think of some more!

Make multiple battleships: you'll need to be careful because you 
need to make sure that you don’t place battleships on top of 
each other on the game board. You'll also want to make sure that 
you balance the size of the board with the number of ships so 
the game is still challenging and fun to play.

Make battleships of different sizes: this is trickier than it 
sounds. All the parts of the battleship need to be vertically or 
horizontally touching and you’ll need to make sure you don’t 
accidentally place part of a ship off the side of the board.

Make your game a two-player game.

Use functions to allow your game to have more features like 
rematches, statistics and more!

Some of these options will be easier after we cover loops in the 
next lesson. Think about coming back to Battleship! after a few 
more lessons and see what other changes you can make!
'''

from random import randint

board = []

print "Welcome to Battleship!"
print "Let's set up the board."

number_of_rows = int(raw_input("Number of rows:"))
number_of_cols = int(raw_input("Number of cols:"))
number_of_turns = int(raw_input("Number of turns:"))
debug = raw_input("Type y to turn on debug mode:")

for x in range(number_of_rows):
    board.append(["O"] * number_of_cols)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

if debug == "y":
    print "Ship loc: %s, %s" % (ship_row, ship_col)

print "Let's get started!"

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

for turn in range(number_of_turns):
    
    print "Turn", turn + 1

    print_board(board)

    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
        
    else:
        if guess_row not in range(number_of_rows) or \
        guess_col not in range(number_of_cols):
            print "Oops, that's not even in the ocean."
            
        elif (board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

    if turn == number_of_turns - 1:
        print "Game Over"


