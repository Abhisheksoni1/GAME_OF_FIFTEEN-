# GAME_OF_FIFTEEN-
COMMAND LINE VERSION OF THE POPULAR GAME 

Fifteen:
Board will always be a square of dimension = board_dimension * board_dimension
>>> python fifteen.py <board_dimension>

4 functions:

1 = init:
Initializes boad = creates a 2-D list int the decreasing order with the blank tile at the bottom-right position
if the dimensions of the board is even the position of one and two will be swaped!

2 = draw:
Draw the current state of the board
Make sure the numbers are formatted correctly each taking exaclty 4 characters wide

3 = move:
Takes the input as the mathematical number of the tile not the index in the array/list
Only the legal moves will change the state of the board, others will provide the repeat input msg
If the move is legal the tile will be moved 

4 = win:
If the state of the board is in the decreasing order, at any point of time, the user gets the congratulations msg and the game quits
