# Project: Squeeze Game
# Intelligent Systems

import random

# Declaring size of the board
board_size = 8

# Game board list
gs = []
# Starting and ending position list of AI Player
ai_start_pos = []
ai_end_pos = []


# Initializing the game board with pieces and an AI start list with possible moves
def initialize():
    for i in range(0, board_size):
        gs.append([])
        for j in range(0, board_size):
            gs[i].append(' -')
            ai_end_pos.append((i, j))
            if i == 0:
                gs[i][j] = ' o'
            if i == 7:
                gs[i][j] = ' •'
        ai_start_pos.append((0, i))
        print()
    return gs


# Displaying the initialised board
def print_board(gs):
    i = 0
    global board_size
    print("|  0  1  2  3  4  5  6  7 |")
    for row in gs:
        rowprint = ' '
        print(i, end="")
        for element in row:
            rowprint += element
            rowprint += ' '
        print(rowprint)
        i = i + 1


# Function to capture move from the user
def selectmove(xoro):

    global board_size
    global gs
    hold = 1
    error = 0

    print(xoro, " Move!")
    if xoro == ' •':
        try:
            x, y = map(int, input("Enter Starting Position: ").split())
        except ValueError:
            error = 1
        try:
            x1, y1 = map(int, input("Enter Ending Position: ").split())
        except ValueError:
            error = 1
        if error == 1:
            print('Wrong Input')
            selectmove(xoro)
        if isvalid(x, y, x1, y1, xoro):
            make_a_move(x, y, x1, y1, xoro)
        else:
            selectmove(xoro)
    else:
        max_r()


# Function to make a move from starting position to ending position
def make_a_move(x, y, x1, y1, xoro):
    # if xoro == ' •':
    gs[x][y] = ' -'
    gs[x1][y1] = xoro
    horizontal_checker(x1, y1)
    vertical_checker(x1, y1)


# Function to find the valid starting value at max risk
def max_r():
    index = random.randrange(0, len(ai_start_pos) - 1, 1)
    start_move = ai_start_pos[index]

    # If 'o' player is already present at the starting position:
    if gs[start_move[0]][start_move[1]] == ' o':
        # Getting the valid ending position of AI
        end_move = min_r(start_move)
        ai_start_pos.append((end_move[0], end_move[1]))

        # Checking validity of the selected move and if found valid then placing it on board
        if isvalid(start_move[0], start_move[1], end_move[0], end_move[1], ' o'):
            ai_start_pos.remove(start_move)
            ai_start_pos.append((end_move))
            # Making the final move for AI
            make_a_move(start_move[0], start_move[1], end_move[0], end_move[1], ' o')
        else:
            max_r()
    else:
        ai_start_pos.remove(start_move)
        max_r()


# Function to find the valid ending position at min risk
def min_r(start_move):
    while True:
        index = random.randrange(0, len(ai_end_pos) - 1, 1)
        coordinates = ai_end_pos[index]
        if gs[coordinates[0]][coordinates[1]] == ' -':
            break
    return coordinates


# Function to check validity of a move
def isvalid(x, y, x1, y1, xoro):
    valid = False

    # Board Boundary Check
    if (0 <= x < board_size) and (0 <= y < board_size):
        valid = True
    else:
        if xoro != ' o':
            print("You have entered wrong position")
        valid = False
    if valid and (0 <= x1 < board_size) and (0 <= y1 < board_size):
        valid = True
    else:
        if xoro != ' o':
            print("Going out of board dimension")
        valid = False

    # Restricted Movement for diagonal movement Check
    if valid and y1 == y or x1 == x:
        valid = True
    else:
        if xoro != ' o':
            print("Restricted Diagonal Movement")
        valid = False

    if valid and gs[x][y] != xoro:
        print("Not your turn!")
        valid = False

    # Selection of starting move is correct and ending position is empty
    if valid and xoro == gs[x][y] and gs[x1][y1] == ' -':
        valid = True

    # Checking ending position
    if valid and gs[x1][y1] != ' -':
        if xoro != ' o':
            print("Piece already present, Try again!")
        valid = False

    # Restricted jump movement
    if valid and not cross_movement(x, y, x1, y1):
        valid = True
    else:
        if xoro != ' o':
            print("Can't jump over other players")
        valid = False
    return valid


# Function to check if a piece is not jumping over another piece which is against game rule
def cross_movement(x, y, x1, y1):
    crossing = False
    initial_position = 0
    end_position = 0

    # Checking validity in case of horizontal movement
    if x == x1:
        if y > y1:
            initial_position = y1 + 1
            end_position = y
        else:
            initial_position = y + 1
            end_position = y1
        for i in range(initial_position, end_position):
            if gs[x][i] != ' -':
                crossing = True
                break

    # Checking validity in case of vertical movement
    if y == y1:
        if x > x1:
            initial_position = x + 1
            end_position = x1
        else:
            initial_position = x + 1
            end_position = x1
        for i in range(initial_position, end_position):
            if gs[i][y] != ' -':
                crossing = True
                break

    return crossing


# Function to check outward squeeze pattern in horizontal direction
def out_horizontal_squeeze(x1, y1, left_status, right_status, hori_counter):
    # left checker for pattern
    left_y = -1
    right_y = -1
    temp = y1 - 1
    if temp >= 0:
        while temp >= 0 and gs[x1][y1] == gs[x1][temp]:
            temp = temp - 1
        if temp < 0:
            temp = temp + 1
        if gs[x1][temp] != ' -' and gs[x1][temp] != gs[x1][y1]:
            left_y = temp
        if left_y != -1:
            print("Found the different left element")
            left_status = True

    # Right checker for pattern
    temp = y1 + 1
    if temp <= 7:
        while temp <= 7 and gs[x1][y1] == gs[x1][temp]:
            temp = temp + 1
        if temp == 8:
            temp = temp - 1
        if gs[x1][temp] != ' -' and gs[x1][temp] != gs[x1][y1]:
            right_y = temp
        if right_y != -1:
            print("Found the different right element")
            right_status = True

    # If both the status are found true, then delete the outward element of opponent player
    if right_status and left_status:
        hori_counter = hori_counter + 1
        gs[x1][left_y] = ' -'
        gs[x1][right_y] = ' -'
        print("SQUEEZED while being in a pattern!")


# Inward squeeze pattern in horizontal direction
def in_horizonatal_squeeze(x1, y1, hori_counter):
    # left checker in horizontal direction
    temp = y1 - 1
    left_y, right_y = -1, -1
    if temp >= 0:
        while temp >= 0 and gs[x1][y1] != gs[x1][temp] and gs[x1][temp] != ' -':
            temp = temp - 1

        if gs[x1][y1] == gs[x1][temp]:
            left_y = temp

        if left_y != -1 and y1 - left_y > 1:
            hori_counter = hori_counter + 1
            for i in range(left_y + 1, y1):
                gs[x1][i] = ' -'
            print("Squeezing while forming a pattern LEFT")

    # Right checker in horizontal Direction
    temp = y1 + 1
    if temp < 7:
        while temp < 7 and gs[x1][y1] != gs[x1][temp] and gs[x1][temp] != ' -':
            temp = temp + 1

        if gs[x1][y1] == gs[x1][temp]:
            right_y = temp

        if right_y != -1 and right_y - y1 > 1:
            hori_counter = hori_counter + 1
            for i in range(y1 + 1, right_y):
                gs[x1][i] = ' -'
            print("Squeezing while forming a pattern RIGHT")


# Main horizontal checker for calling both the horizontal checker functions
def horizontal_checker(x1, y1):
    hori_counter = 0
    left_status, right_status = False, False

    # outward squeeze
    out_horizontal_squeeze(x1, y1, left_status, right_status, hori_counter)

    # inward squeeze
    in_horizonatal_squeeze(x1, y1, hori_counter)


# Outward squeeze pattern in vertical direction
def out_vertical_squeeze(x1, y1, up_status, down_status, vert_counter):
    # Up checker
    up_x = -1
    down_x = -1
    temp = x1 - 1
    if temp >= 0:
        while temp >= 0 and gs[x1][y1] == gs[temp][y1]:
            temp = temp - 1
        if temp < 0:
            temp = temp + 1
        if gs[temp][y1] != ' -' and gs[temp][y1] != gs[x1][y1]:
            up_x = temp
        if up_x != -1:
            print("Found the different up element: Vertical Checker")
            up_status = True

    # Down checker
    temp = x1 + 1
    if temp <= 7:
        while temp <= 7 and gs[x1][y1] == gs[temp][y1]:
            temp = temp + 1
        if temp == 8:
            temp = temp - 1
        if gs[temp][y1] != ' -' and gs[temp][y1] != gs[x1][y1]:
            down_x = temp
        if down_x != -1:
            print("Found the different down element Vertical Checker")
            down_status = True

    # Checking if both the status are valid
    if up_status and down_status:
        vert_counter = vert_counter + 1
        gs[up_x][y1] = ' -'
        gs[down_x][y1] = ' -'
        print("SQUEEZED while being in a pattern!")


# End points of squeeze pattern in vertical direction
def in_vertical_checker(x1, y1, vert_counter):
    # Up Checker
    temp = x1 - 1
    up_x, down_x = -1, -1
    if temp >= 0:
        while temp >= 0 and gs[x1][y1] != gs[temp][y1] and gs[temp][y1] != ' -':
            temp = temp - 1
        if temp < 0:
            temp = temp+1
        if gs[x1][y1] == gs[temp][y1] :
            up_x = temp
            print("Founding Pattern!")

        if up_x != -1 and x1 - up_x > 1:
            vert_counter = vert_counter + 1
            for i in range(up_x + 1, x1):
                gs[i][y1] = ' -'
            print("Squeezing while forming a pattern UP")

    # Down Checker
    temp = x1 + 1
    up_x, down_x = -1, -1
    if temp < 7:
        while temp < 7 and gs[x1][y1] != gs[temp][y1] and gs[temp][y1] != ' -':
            temp = temp + 1

        if gs[x1][y1] == gs[temp][y1]:
            down_x = temp

        if down_x != -1 and down_x - x1 > 1:
            vert_counter = vert_counter + 1
            for i in range(x1 + 1, down_x):
                gs[i][y1] = ' -'
            print("Squeezing while forming a pattern DOWN")


# Main vertical checker for calling both the horizontal checker functions
def vertical_checker(x1, y1):
    vert_counter = 0
    up_status, down_status = False, False
    out_vertical_squeeze(x1, y1, up_status, down_status, vert_counter)
    in_vertical_checker(x1, y1, vert_counter)

# Function to calculate the total number of pieces remaining on board
def max_pieces():
    total_x = 0
    total_o = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if gs[i][j] == ' o':
                total_o = total_o + 1
            if gs[i][j] == ' •':
                total_x = total_x + 1
    return total_x, total_o

# Function to check if the game has ended and who is the winner
def is_game_ended(x_moves, o_moves):
    total_x, total_o = max_pieces()
    ended = False
    winner = None

    # Moves Exhausted
    if x_moves < 1 or o_moves < 1:
        ended = True
        if total_x > total_o:
            winner = ' •'
        elif total_o > total_x:
            winner = ' o'
        else:
            winner = None

    # Players Eliminated
    if total_x == 0 and total_o == 0:
        ended = True
        winner = None
    if total_x == 0 and total_o != 0:
        ended = True
        winner = ' o'
    if total_o == 0 and total_x != 0:
        ended = True
        winner = ' •'
    return ended, winner


# Main Function
def main():
    # xoro : Current turn of which player
    global xoro
    # Starting turn
    # ' •' for user
    # ' o' for AI
    xoro = ' •'
    gs = initialize()
    x_moves = 10
    o_moves = 10

    while True:
        ended, winner = is_game_ended(x_moves, o_moves)
        print_board(gs)
        if not ended:
            if xoro == ' o':
                selectmove(xoro)
                xoro = ' •'
                o_moves = o_moves - 1
            else:
                selectmove(xoro)
                xoro = ' o'
                x_moves = x_moves - 1
        else:
            print("Winner is ---->", winner)
            break


main()
