from __future__ import print_function
import random

def display_board(board):
    """Takes in a list from 1-9 and prints out the current game board"""

    print(' %s | %s | %s ' % (board[1], board[2], board[3]))
    print('---|---|---')
    print(' %s | %s | %s ' % (board[4], board[5], board[6]))
    print('---|---|---')
    print(' %s | %s | %s ' % (board[7], board[8], board[9]))

def player_input():
    """Asks for Player 1 to pick X or O marker"""

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    """Places the marker on the board"""

    board[position] = marker

def win_check(board, mark):
    """Checks the current board if there is a winner"""

    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))

def choose_first():
    """Randomly chooses who starts first"""

    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    """Returns a boolean if current position on board is taken."""

    return board[position] == ' '

def full_board_check(board):
    """Returns true if space_check() returns false"""

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    """Asks the player where they would like to move then returns position."""

    position = ' '

    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Choose you position: (1-9)')
    return int(position)

def replay():
    """Asks if player wants to play another game."""

    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
