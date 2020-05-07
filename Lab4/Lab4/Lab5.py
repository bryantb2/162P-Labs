# library imports
import random;
import constant;
import copy;


# Board variables
board_col_number = 9; 
board_row_number = 14;


"""
Here are a list of all my functions and how they related to the functions required in lab 5:
    - getSize() relates to the top-level board variables at the top of this file
    - displayInstructions() relates to print_instructions()
    - userDefinedSize() relates to the function prompt_and_set_user_size()
    - createMap() relates to build_board() and fill_dungeon()
    - validYesNo() relates to validate_yes_no()
    - placeTrap(), ect. relates to generate_dungeon()
    - findEmpty() relates to find_empty_square()
    - findPlayer() relates to get_player_position()
    - getMove() relates to translate_move_to_indexes()
    - checkBounds() relates to move_out_of_bounds()
    - checkWin/loss() relates to check_if_collides()
    - updateMap() relates to make_player_move()
"""


# Basic UI Prints
def print_dungeon_board(dungeon):
    print('Dungeon board is: ');
    for row in range(board_row_number):
        column_string = '[';
        for col in range(board_col_number):
            board_value = dungeon[col][row];
            column_string += (str(board_value) + ', ' if col != (board_col_number - 1) else str(board_value) + ']');
        print(column_string);

def print_instructions():
    print("------------- Instructions -------------");
    print('The dungeon crawler game involves a computer-generated board filled with traps, marked as ' + constant.trap_symbol + ", that must be avoided as you \n");
    print("the player, marked as " + constant.player_symbol + ", " + "traverse the board towards the treasure, marked as " + constant.treasure_symbol + ". \n");
    print("To win, you must safety move left, right, up, or down to the treasure, without touching the traps. \n")
    print("Note that the empty squares, marked as " + constant.empty_square_symbol + " are safe to come in contact with, and should be the only squares you touch. \n");
    print("Remeber: you can end the game at any time by typing 'quit'.")
    print("------------- Begin Game ------------- \n");

def print_inbound_moves_UI_string(move_arr):
    UI_string = '';
    for index in range(len(move_arr)):
        UI_string += move_arr[index] + (', ' if index != len(move_arr) - 1 else '');
    print('Move not within game bounds. Only the following moves are valid, given your position: ' + UI_string);

def print_available_move_types():
    move_string = constant.move_left + ', ' + constant.move_right + ', ' + constant.move_up + ', ' + constant.move_down;
    print('Invalid move type. Only the following move characters can be used: ' + move_string + '.')

def print_move(move_type):
    move_string = '';
    if(move_type == constant.move_left):
        move_string = 'left';
    elif(move_type == constant.move_right):
        move_string = 'right';
    elif(move_type == constant.move_down):
        move_string = 'down';
    else:
        move_string = 'up';
    print('You move one space to the ' + move_string);


# Translate move to index
def translate_move_to_indexes(dungeon, current_player_pos, move_type):
    # get current player position
    # special case: the higher the row number, the further down the board the space is. Compensate by subtracting instead of adding or visa versa.
    row_pos = current_player_pos["row"];
    col_pos = current_player_pos["col"];
    move_dictionary = { "row": 0, "col": 0 };
    if(constant.move_left == move_type):
        move_dictionary["row"] = row_pos;
        move_dictionary["col"] = col_pos - 1;
    elif(constant.move_right == move_type):
        move_dictionary["row"] = row_pos;
        move_dictionary["col"] = col_pos + 1;
    elif(constant.move_up == move_type):
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
    dungeon[old_col_pos][old_row_pos] = constant.empty_square_symbol;
    dungeon[new_col_pos][new_row_pos] = constant.player_symbol;
    return dungeon;


# Get player position
def get_player_position(dungeon):
    for col in range(board_col_number):
        for row in range(board_row_number):
            current_board_value = dungeon[col][row];
            if(current_board_value == constant.player_symbol):
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
    if(move_string == constant.move_left or move_string == constant.move_right 
       or move_string == constant.move_down or move_string == constant.move_up):
        return True;
    return False;


# UI helpers
def prompt_and_set_user_size():
    # method handles the setting of user-defined board values    
    # check if user wants to proceed and set values
    # check if the user answered yes, then set all values
    global board_col_number;
    global board_row_number;
    should_set_board = False;
    has_answered = False;
    while(has_answered == False):
        should_have_custom_board = prompt_user("Before starting the game, would you like to specify the size of the board? Type Y or N: ");
        if(validate_yes_no(should_have_custom_board)):
            has_answered = True;
            should_set_board = True if should_have_custom_board == "Y" else False;
        else:
            print('Please enter a valid value');
    if(should_set_board):
        prompt_message_one = "Please select a board height. Must be a number greater than 5 but less than or equal to 20: ";
        prompt_message_two = "Please select a board width. Must be a number greater than 5 but less than or equal to 20: ";
        lower_bound = 5;
        upper_bound = 20;
        custom_height = prompt_return_board_number(prompt_message_one, lower_bound, upper_bound);
        custom_width = prompt_return_board_number(prompt_message_two, lower_bound, upper_bound);
        board_col_number = custom_width;
        board_row_number = custom_width;
    else:
        board_col_number = 9; 
        board_row_number = 14;

def prompt_return_board_number(prompt_message, lower_bound, upper_bound):
    has_answered = False;
    chosen_value = 0;
    while(has_answered == False):
        custom_value = prompt_user(prompt_message);
        if(validate_user_number(custom_value)):
            if(validate_user_board_value_inbounds(custom_value, lower_bound, upper_bound)):
                has_answered = True;
                chosen_value = int(custom_value);
            else:
                print('Try again. Value must be within ' + str(lower_bound) + ' and ' + str(upper_bound) + '.');
        else:
            print('Try again. Value must be an actual number.');
    return chosen_value;

def prompt_user(prompt_message):
    return input(prompt_message);

def return_inbound_moves(dungeon, current_position_indexes):
    # return an array of all the valid move symbols
    row = current_position_indexes["row"];
    col = current_position_indexes["col"];
    validate_move_arr = [];
    # make moves to get indexes
    moved_left = translate_move_to_indexes(dungeon, current_position_indexes, constant.move_left);
    moved_right = translate_move_to_indexes(dungeon, current_position_indexes, constant.move_right);
    moved_up = translate_move_to_indexes(dungeon, current_position_indexes, constant.move_up);
    moved_down = translate_move_to_indexes(dungeon, current_position_indexes, constant.move_down);
    # test if moves are within bounds
    if(move_out_of_bounds(moved_left) == False):
        validate_move_arr.append(constant.move_left);
    if(move_out_of_bounds(moved_right) == False):
        validate_move_arr.append(constant.move_right);
    if(move_out_of_bounds(moved_up) == False):
        validate_move_arr.append(constant.move_up);
    if(move_out_of_bounds(moved_down) == False):
        validate_move_arr.append(constant.move_down);
    # return move list
    return validate_move_arr;


# Raw input validators
def validate_yes_no(user_input):
    if(user_input.upper() == "Y" or user_input.upper() == "N"):
        return True;
    return False;

def validate_quit(user_input):
    if(user_input.upper() == "QUIT"):
        return True;
    return False;

def validate_user_number(user_input):
    # makes sure the user number is actually a number
    if(user_input.isdigit()):
        return True;
    return False;

def validate_user_board_value_inbounds(user_input, lower_bound, upper_bound):
    number_as_int = int(user_input);
    if(number_as_int > lower_bound and number_as_int <= upper_bound):
        return True;
    return False;


# Handlers
def handle_play_again():
    # this will restart the game if user answers yes
    should_restart = False;
    has_answered = False;
    while(has_answered == False):
        restarted_game = prompt_user('Would you like to restart the game? Type Y or N: ');
        if(validate_yes_no(restarted_game)):
            has_answered = True;
            should_restart = True if restarted_game == "Y" else False;
        else:
            print('Please enter a valid value.');
    if(should_restart):
        handle_board_setup();

def handle_board_setup():
    # check if user wants to set custom board size
    # generate dungeona
    # print instructions
    # print board
    # start game
    prompt_and_set_user_size();
    dungeon = generate_dungeon();
    print_dungeon_board(dungeon);
    handle_move(dungeon, prompt_user('Please make your first move. Use L, R, U, or D to traverse the board: '));

def handle_move(dungeon, move_type):
    # check if user wants to quit
    if(validate_quit(move_type) == False):
        # get current player pos
        current_pos = get_player_position(dungeon);
        # validate input
        if(is_valid_move_type(move_type)):
            # translate move to indexes
            # check if within bounds
            move_indexes = translate_move_to_indexes(dungeon, current_pos, move_type);
            if(move_out_of_bounds(move_indexes) == False):
                # check for win loss conditions
                if(check_if_collides(dungeon, move_indexes, constant.trap_symbol)):
                    # show board
                    # prompt to play again
                    new_dungeon = make_player_move(dungeon, current_pos, move_indexes);
                    print_dungeon_board(new_dungeon);
                    print('You moved onto a trap! Game over.');
                    handle_play_again();
                elif(check_if_collides(dungeon, move_indexes, constant.treasure_symbol)):
                    # show board
                    # prompt to play again
                    new_dungeon = make_player_move(dungeon, current_pos, move_indexes);
                    print_dungeon_board(new_dungeon);
                    print('You got to the treasure. Congrats, you have won!');
                    handle_play_again();
                else:
                    # make move
                    # print move
                    # show board
                    new_dungeon = make_player_move(dungeon, current_pos, move_indexes);
                    print_move(move_type);
                    print_dungeon_board(new_dungeon);
                    # Call handle game and pass in new move value
                    handle_move(new_dungeon, prompt_user('Please enter a valid move character: '));
            else: 
                # Print errors and prompt for new move value
                print_inbound_moves_UI_string( return_inbound_moves(dungeon, current_pos) );
                move_input = prompt_user('Please enter move character within game bounds: ');
                # Call handle game and pass in new move value
                handle_move(dungeon, move_input);
        else:
            # Print errors and prompt for new move value
            print_available_move_types();
            move_input = prompt_user('Please enter a valid move character: ');
            # Call handle game and pass in new move value
            handle_move(dungeon, move_input);
    else:
        handle_play_again();


# Board generators
def generate_dungeon():
    # Create array based on dimensions at top of file
    # Generate set number of traps
    # Place treasure and player
    base_dungeon = fill_dungeon(build_board(board_col_number), board_row_number);
    base_dungeon = add_player_and_treasure(add_traps_to_blank_board(base_dungeon, 4));
    return base_dungeon;

def find_empty_square(dungeon, col_limit, row_limit):
    # will randomly find a square within bounds of the row and column numbers
    # square is considered empty if it doesn't have anything other than the empty square symbol on it
    empty_square_found = False;
    square_indexes = copy.deepcopy(constant.move_dic_structure);
    while(empty_square_found == False):
        random_row = random.randrange(0, row_limit, 1);
        random_col = random.randrange(0, col_limit, 1);
        square_value = dungeon[random_col][random_row];
        if(square_value != constant.trap_symbol and square_value != constant.player_symbol and square_value != constant.treasure_symbol):
            empty_square_found = True;
            square_indexes["row"] = random_row;
            square_indexes["col"] = random_col;
    return square_indexes;

def find_add_entity_to_empty_square(dungeon, entity_symbol, col_limit, row_limit):
    # call find empty square
    # set dungeon, with indexes, to symbol
    # return updated dungeon
    empty_square_indexes = find_empty_square(dungeon, col_limit, row_limit);
    row = empty_square_indexes["row"];
    col = empty_square_indexes["col"];
    dungeon[col][row] = entity_symbol;
    return dungeon;

def fill_dungeon(dungeon_structure, height):
    # height is required to generate the proper number of rows in the dungeon structure
    for col_num in range(len(dungeon_structure)):
        height_num = 0;
        for height_num in range(height):
            dungeon_structure[col_num].append(constant.empty_square_symbol);
    return dungeon_structure;

def build_board(width):
    # only width is required to generate the correct matrix structure
    board = [];
    i = 0;
    while(i < width):
        board.append([]);
        i += 1;
    return board;

def add_traps_to_blank_board(blank_dungeon, trap_number):
    # will build dungeon with player, treasure, and trap symbols
    # loop through trap number
    # get square indexes and set it to trap
    current_trap = 0;
    while current_trap < trap_number:
        blank_dungeon = find_add_entity_to_empty_square(blank_dungeon, constant.trap_symbol, board_col_number, board_row_number);
        current_trap += 1;
    return blank_dungeon;

def add_player_and_treasure(trap_fill_dungeon):
    # get indexes for player and treasure
    player_created = False;
    treasure_created = False;
    # add player
    trap_fill_dungeon = find_add_entity_to_empty_square(trap_fill_dungeon, constant.player_symbol, board_col_number, board_row_number);
    # add treasure
    trap_fill_dungeon = find_add_entity_to_empty_square(trap_fill_dungeon, constant.treasure_symbol, board_col_number, board_row_number);
    # return board
    return trap_fill_dungeon;


# Call main if script is being executed and not imported
def main():
    handle_board_setup();

if(__name__ == "__main__"):
    main();