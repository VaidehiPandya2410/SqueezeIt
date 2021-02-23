# SqueezeIt
Project: Squeeze-it
Category: Game Playing, Intelligent Systems
Class Project
Game Overview:
Squeeze-it is a two-player board game with a board size of 8x8. Each play initially has eight pieces placed on the uppermost and lowermost row. The initial configuration of the game looks like this:




Programming Language: Python
System requirements: 
Disk space: 1 GB.
Operating systems: Windows* 7 or later, macOS, and Linux.
Python versions: 2.7.X, 3.6.X.

Program file included: squeezeAI.py
Game Play: Since it’s a two-player game, match can either be played between AI-human or human-human. Each player can pick a piece from any valid location and place it on a blank position. 
Pieces can be squeezed in two cases:  
If the opponent captures the pieces of another player in inward direction.
If the opponent squeezes the pieces in outward direction.
If both cases are valid, then both the squeezes will take place.
Installation Instructions:
A Python IDE is required to run the program.
Configuration Instructions: 
Each time a user turn takes place, program will ask the user for starting position and ending position. These positions are stored in tuple and will be input in this format: starting_position_coordinate1<space>ending_position_coordinate2


Program Overview:
Movement Restrictions: Horizontal and vertical on Non-empty positions without crossing over the opponent.

Functions used:
initialize() : For initializing the game board with default values
print_board(): For displaying the initialized board.
selectmove(): For capturing the move from the user.
make_a_move() : For making a move from starting to ending position.
isvalid(): For checking the validity of each move of the opponent.
cross_movement() : For ensuring that a move doesn’t do cross movement over another piece.
out_horizontal_squeeze(): For checking outward horizontal squeeze pattern.
in_horizontal_squeeze(): For checking inward horizontal squeeze pattern. 
horizontal_checker(): For calling both the horizontal checkers.
out_vertical_squeeze(): For checking outward horizontal squeeze pattern.
in_vertical_squeeze(): For checking inward horizontal squeeze pattern 
vertical_checker(): For checking both the vertical checkers.
max_pieces(): For calculating maximum number of pieces present on the board. 
is_game_ended() : For checking maximum pieces remaining and deciding if the game ended and who is the winner.
max_r(): For calculating the starting position for AI which is at maximum risk.
min_r(): For calculating the minimum position for AI which is at the minimum risk.
main(): Main function

Validations are placed on the following cases:
If the input value is incorrect
If the piece is placed on non-empty position.
If the piece tries to move out of board boundary.
If the piece tries diagonal movement
Restricted Jump movement
Left, Right, Up and Down range checker

Game Ending conditions:
If all the moves are exhausted
If the Player is eliminated
In either case, Player with the maximum pieces on the board wins.

Team Members:
Apoorva Tyagi – aptyagi@ttu.edu
Vaidehi Pandya – vaidehi.pandya@ttu.edu
Nitisha Patange --  nitisha.patange@ttu.edu
