# Board variables
trap_symbol = 'T';
treasure_symbol = 'X';
player_symbol = 'G';
empty_square_symbol = '*';
board_col_number = 9; 
board_row_number = 14;
move_left = 'L';
move_right = 'R';
move_up = 'U';
move_down = 'D';

# Print board
def print_dungeon_board(dungeon):
    print('Dungeon board is: ');
    for row in range(board_row_number):
        column_string = '[';
        for col in range(board_col_number):
            board_value = dungeon[col][row];
            column_string += (str(board_value) + ', ' if col != (board_col_number - 1) else str(board_value) + ']');
        print(column_string);


# Translate move to index
def translate_move_to_indexes(dungeon, current_player_pos, move_type):
    # get current player position
    # special case: the higher the row number, the further down the board the space is. Compensate by subtracting instead of adding or visa versa.
    row_pos = current_player_pos["row"];
    col_pos = current_player_pos["col"];
    move_dictionary = { "row": 0, "col": 0 };
    if(move_left):
        move_dictionary["row"] = row_pos;
        move_dictionary["col"] = col_pos - 1;
    elif(move_right):
        move_dictionary["row"] = row_pos;
        move_dictionary["col"] = col_pos + 1;
    elif(move_up):
        move_dictionary["row"] = row_pos - 1;
        move_dictionary["col"] = col_pos;
    else:
        move_dictionary["row"] = row_pos + 1;
        move_dictionary["col"] = col_pos;
    return move_dictionary;


# Make move and change board
def make_player_move(dungeon, current_player_position, move_indexes):
    # make move
    # fill old space with standard square marker
    old_row_pos = current_player_position["row"];
    old_col_pos = current_player_position["col"];
    new_row_pos = move_indexes["row"];
    new_col_pos = move_indexes["col"];
    dungeon[old_col_pos][old_row_pos] = empty_square_symbol;
    dungeon[new_col_pos][new_row_pos] = player_symbol;
    return dungeon;


# Get player position
def get_player_position(dungeon):
    for col in range(board_col_number):
        for row in range(board_row_number):
            current_board_value = dungeon[col][row];
            if(current_board_value == player_symbol):
                return { "row": row, "col": col };
    return None;


# Move validators
def check_if_collides(dungeon, move_indexes, collision_symbol):
    # Check if the next move will hit the specified collision symbol
    row = move_indexes["row"];
    col = move_indexes["col"];
    new_move_value = dungeon[col][row];
    if(new_move_value == collision_symbol):
        return True;
    else:
        return False;

def move_out_of_bounds(move_indexes):
    # check if the move indexes are within the max row/col length and greater than or equal to 0
    row = move_indexes["row"];
    col = move_indexes["col"];
    if(row >= board_row_number or col >= board_col_number 
       or row < 0 or col < 0):
        return True;
    return False;

def is_valid_move_type(move_string):
    if(move_string == move_left or move_string == move_right 
       or move_string == move_down or move_string == move_up):
        return True;
    return False;


# UI helper
def return_inbound_moves(dungeon, current_position_indexes):
    # return an array of all the valid move symbols
    row = current_position_indexes["row"];
    col = current_position_indexes["col"];
    validate_move_arr = [];
    # make moves to get indexes
    moved_left = translate_move_to_indexes(dungeon, current_position_indexes, move_left);
    moved_right = translate_move_to_indexes(dungeon, current_position_indexes, move_right);
    moved_up = translate_move_to_indexes(dungeon, current_position_indexes, move_up);
    moved_down = translate_move_to_indexes(dungeon, current_position_indexes, move_down);
    # test if moves are within bounds
    if(move_out_of_bounds(moved_left)):
        validate_move_arr.append(move_left);
    elif(move_out_of_bounds(moved_right)):
        validate_move_arr.append(move_right);
    elif(move_out_of_bounds(moved_up)):
        validate_move_arr.append(move_up);
    elif(move_out_of_bounds(moved_down)):
        validate_move_arr.append(move_down);
    # return move list
    return validate_move_arr;

def prompt_move(prompt_message):
    return input(prompt_message);

def print_inbound_moves_UI_string(move_arr):
    UI_string = '';
    for index in range(move_arr.count()):
        UI_string += move_arr[index] + (', ' if index != move_arr.count() - 1 else '');
    print('Move not within game bounds. Only the following moves are valid, given your position: ' + UI_string);

def print_available_move_types():
    move_string = move_left + ', ' + move_right + ', ' + move_up + ', ' + move_down;
    print('Invalid move type. Only the following move characters can be used: ' + move_string + '.')

def print_move(move_type):
    move_string = '';
    if(move_type == move_left):
        move_string = 'left';
    elif(move_type == move_right):
        move_string = 'right';
    elif(move_type == move_down):
        move_string = 'down';
    else:
        move_string = 'up';
    print('You move one space to the ' + move_string);

# Handle move
def handle_move(dungeon, move_type):
    # get current player pos
    current_pos = get_player_position(dungeon);
    # validate input
    if(is_valid_move_type(move_type)):
        # translate move to indexes
        # check if within bounds
        move_indexes = translate_move_to_indexes(dungeon, current_pos, move_type);
        if(move_out_of_bounds(move_indexes) == False):
            # check for win loss conditions
            if(check_if_collides(dungeon, move_indexes, trap_symbol)):
                # show board
                print_dungeon_board(dungeon);
                print('You moved onto a trap! Game over.');
            elif(check_if_collides(dungeon, move_indexes, treasure_symbol)):
                # show board
                print_dungeon_board(dungeon);
                print('You got to the treasure. Congrats, you have won!');
            else:
                # make move
                new_dungeon = make_player_move(dungeon, current_pos, move_indexes);
                # print move
                # show board
                print_move(move_type);
                print_dungeon_board(new_dungeon);
                move_input = prompt_move('Please enter a valid move character: ');
                # Call handle game and pass in new move value
                handle_move(new_dungeon, move_input);
        else: 
            # Print errors and prompt for new move value
            print_inbound_moves_UI_string( return_inbound_moves(dungeon, current_pos) );
            move_input = prompt_move('Please enter move character within game bounds: ');
            # Call handle game and pass in new move value
            handle_move(dungeon, move_input);
    else:
        # Print errors and prompt for new move value
        print_available_move_types();
        move_input = prompt_move('Please enter a valid move character: ');
        # Call handle game and pass in new move value
        handle_move(dungeon, move_input);


# Board generators
def generate_dungeon():
    # Create array based on dimensions at top of file
    # Generate set number of traps
    # Place treasure and player
    dungeon_board = build_board;
    base_dungeon = fill_dungeon(build_board(board_col_number), board_row_number);

def fill_dungeon(dungeon_structure, height):
    # height is required to generate the proper number of rows in the dungeon structure
    for col in dungeon_structure:
        height_num = 0;
        while(i < height):
            col.append(empty_square_symbol);
    return dungeon_structure;

def build_board(width):
    # only width is required to generate the correct matrix structure
    board = [];
    i = 0;
    while(i < width):
        board.append([]);
        i += 1;
    return board;

# Entity generators
def add_traps_to_blank_board(blank_dungeon, trap_number):
    # will build dungeon with player, treasure, and trap symbols
    # loop through trap number
    # create loop to generate indexes for trap
        # generate random numbers for trap indexes
        # if indexes already a trap, repeat
    current_trap = 0;
    while current_trap < trap_number:
        trap_not_set = True;
        while trap_not_set == True:
            random_row = random.randrange(0, board_row_number, 1);
            random_col = random.randrange(0, board_col_number, 1);
            if(blank_dungeon[random_col][randomrandom_row] != trap_symbol):
                trap_not_set = False;
                blank_dungeon[random_col][random_row] = trap_symbol;
        current_trap+=1;
    return blank_dungeon;

def add_player_and_treasure(trap_fill_dungeon):
    # create loop to generate player  
        # generate indexes
        # if indexes already a trap, repeat
    # create loop to generate treasure  
        # generate indexes
        # if indexes already a trap OR player, repeat
    player_created = False;
    treasure_created = False;
    # add player
    while player_created == False:
        random_row = random.randrange(0, board_row_number, 1);
        random_col = random.randrange(0, board_col_number, 1);
        target_square = trap_filled_dungeon[random_col][random_row];
        if(trap_fill_dungeon[random_col][random_row] != trap_symbol):
            player_created = True;
            trap_fill_dungeon[random_col][random_row] = player_symbol;
    # add treasure
    while treasure_created == False:
        random_row = random.randrange(0, board_row_number, 1);
        random_col = random.randrange(0, board_col_number, 1);
        target_square = trap_filled_dungeon[random_col][random_row];
        if(trap_fill_dungeon[random_col][random_row] != trap_symbol and trap_fill_dungeon[random_col][random_row] != player_symbol):
            treasure_created = True;
            trap_fill_dungeon[random_col][random_row] = player_symbol
    # return board
    return trap_fill_dungeon;


def reset_game():
    # generate dungeon
    # fill dungeon with entities
    dungeon = generate_dungeon();
    board_with_players_treasure = add_player_and_treasure(add_traps_to_blank_board(dungeon, 4));

    # print instructions
    print('The dungeon crawler game involves a computer-generated board filled with traps, marked as ' + trap_symbol + ", that must be avoided as you " +
    " the player, marked as " + player_symbol + ", traverse the board towards the treasure, marked as " + treasure_symbol + "." + " To win, you must safety move left, right, up, or down to the treasure, without touching the traps. " +
    "Note that the empty squares, marked as " + empty_square_symbol + " are safe to come in contact with, and should be the only squares you touch.");
    # print board
    print_dungeon_board(board_with_players_treasure);
    # start game
    handle_move(board_with_players_treasure, prompt_move('Please make your first move. Use one of the following characters to traverse the board: L, R, U, or D '));


# testing functions
reset_game();