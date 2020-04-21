# Board array and game state
player_one_marker = 'X';
player_two_marker = 'O';


# Game functions
def display_instructions():
    print("This is a game of Tic-Tac-Toe. You will select an empty location and " +
    "enter its index to select a move. The first player will be X and the second will be O.");

def show_board(board):
    # loop through columns (vertical)
    for innerIndex in range(3):
        ui_str = '[';
        # loop through rows (horizontal)
        for outerIndex in range(3):
            ui_str += (', ' if outerIndex != 0 else '') + board[outerIndex][innerIndex];
            if(outerIndex == 2):
                ui_str += ']';
        print(ui_str);

def move_in_range(user_move_number):
    is_in_range = False;
    if(user_move_number >= 1):
        if(user_move_number <= 9):
            return True;
    return False;

def is_square_open(board, square_number):
    indexes = translate_move_to_indexes(square_number);
    row_index = indexes["row"];
    column_index = indexes["column"];
    square_value = board[row_index][column_index];
    # check value in square
    if(square_value == player_one_marker or square_value == player_two_marker):
        return False;
    return True;

def translate_move_to_indexes(user_move_number):
    # converts 1D array index into 2D indexes
    index_vals = { "row": 0, "column": 0 };
    # use tunrary operator to find row index (then subtract 1 because the index is behind the square number)
    row_val = (3 if user_move_number % 3 == 0 else user_move_number % 3) -1;
    col_val = 0;
    if(user_move_number <= 3):
        col_val = 0;
    elif(user_move_number <= 6):
        col_val = 1;
    else:
        col_val = 2;
    index_vals["row"] = row_val;
    index_vals["column"] = col_val;
    return index_vals;

def translate_indexes_to_number(column, row):
    return 3 * row + (column + 1)

def make_move(board, square_number, player_marker):
    indexes = translate_move_to_indexes(square_number);
    row = indexes["row"];
    column = indexes["column"];
    board[column][row] = player_marker;
    return board;

def switch_current_player(current_player):
    if (current_player == player_one_marker):
        return player_two_marker;
    else:
        return player_one_marker

# check board functions
def check_draw(board):
    square_counter = 0;
    for column in range(3):
        for row in range(3):
            square_number = translate_indexes_to_number(column, row);
            if(is_square_open(board, square_number)):
                square_counter += 1;
    if(square_counter == 9):
        return True;
    return False;

def check_winner(board, player_marker):
    if(check_vertical(board, player_marker) 
       or check_horizontal(board, player_marker) 
       or check_diagonals(board, player_marker)):
        return True;
    return False;


def check_vertical(board, player_marker):
    for column in range(3):
        square_counter = 0;
        for row in range(3):
            if(board[column][row] == player_marker):
                square_counter += 1;
        if(square_counter == 3):
            return True;
    return False;

def check_horizontal(board, player_marker):
    for row in range(3):
        square_counter = 0;
        for column in range(3):
            if(board[column][row] == player_marker):
                square_counter += 1;
        if(square_counter == 3):
            return True;
    return False;

def check_diagonals(board, player_marker):
    diags = [[1,5,9],[3,5,7]];
    # go through diagonals
    for diag in diags:
        square_counter = 0;
        for square_num in diag:
            # translate square num to indexes
            square_as_indexes = translate_move_to_indexes(square_num);
            row = square_as_indexes["row"];
            column = square_as_indexes["column"];
            if(board[column][row] == player_marker):
                square_counter += 1;
        if(square_counter == 3):
            return True;
    return False;

# handlers
def handle_game(game_board, square_number, current_player):
    # print current game state
    show_board(game_board);
    # validate inputted number
    if(move_in_range(square_number)):
        # check if square is available
        if(is_square_open(game_board, square_number)):
            # update board
            game_board = make_move(game_board, square_number, current_player);
            # check for winner or draw
            if(check_winner(game_board, current_player)):
                print('Player ' + current_player + ' has won the game!');
            elif(check_draw(game_board)):
                print('Game has ended in a draw!');
            else:
                # swap player
                current_player = switch_current_player(current_player);
                # call game again
                handle_game(game_board, int(square_number), current_player);
        else:
            print('That square has already been used.');
            number = input('Please pick another number: ');
            handle_game(game_board, int(number), current_player);
    else:
        print('That square number is not within range. Must be between 1 and 9');
        number = input('Please pick another number: ');
        handle_game(game_board, int(number), current_player);


def reset_game():
    # set starting values
    game_board = [['1','4','7'],['2','5','8'],['3','6','9']];
    current_turn = player_one_marker;
    # print UI instructions
    display_instructions();
    print('The board looks like:');
    show_board(game_board);
    # start game
    handle_game(game_board, int(input('Player ' + current_turn + ' please enter a square number: ')), current_turn);

# Run Test
reset_game();