
board = {}
turn = 'X'
move = None
winner = False


def format():
    print(' ', 'A', '|', 'B', '|', 'C')
    print('1', board['a1'], '|', board['b1'], '|', board['c1'])
    print('------------')
    print('2', board['a2'], '|', board['b2'], '|', board['c2'])
    print('------------')
    print('3', board['a3'], '|', board['b3'], '|', board['c3'])


def check_winner():
    global winner
    if board['a1'] == 'X' and board['b1'] == 'X' and board['c1'] == 'X':
        winner = True
    elif board['a1'] == 'O' and board['b1'] == 'O' and board['c1'] == 'O':
        winner = True
    elif board['a2'] == 'X' and board['b2'] == 'X' and board['c2'] == 'X':
        winner = True
    elif board['a2'] == 'O' and board['b2'] == 'O' and board['c2'] == 'O':
        winner = True
    elif board['a3'] == 'X' and board['b3'] == 'X' and board['c3'] == 'X':
        winner = True
    elif board['a3'] == 'O' and board['b3'] == 'O' and board['c3'] == 'O':
        winner = True
    elif board['a1'] == 'X' and board['b2'] == 'X' and board['c3'] == 'X':
        winner = True
    elif board['a1'] == 'O' and board['b2'] == 'O' and board['c3'] == 'O':
        winner = True
    elif board['a3'] == 'X' and board['b2'] == 'X' and board['c1'] == 'X':
        winner = True
    elif board['a3'] == 'O' and board['b2'] == 'O' and board['c1'] == 'O':
        winner = True
    else:
        winner = False


def init_game():
    # Use the global keyword to update global variables
    global board, turn, move, winner
    board = {
        'a1': ' ', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': ' ', 'c2': ' ',
        'a3': ' ', 'b3': ' ', 'c3': ' ',
    }
    turn = 'X'
    move = None
    # check that no one has won

    while winner == False:
        move = input('Enter Column A-C and Row 1-3: ')
        # if a move is in the board mark the spot as X
        if move in board and board[move] == ' ':
            board[move] = turn
            check_winner()
            if winner == True:
                print(f"Player: {turn} is the Winner!")
            if turn != 'O':
                turn = 'O'
            else:
                turn = 'X'
        format()


init_game()