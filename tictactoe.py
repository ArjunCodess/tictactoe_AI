"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None

turn = ""


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCounter = 0
    oCounter = 0

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                xCounter += 1
            elif board[i][j] == O:
                oCounter += 1

    if xCounter > oCounter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # i = row & j = column
    possibleAction = []

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possibleAction.append((i, j))

    return possibleAction



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)

    # Get the player making the move using the player function
    player_making_move = player(result_board)

    # Update the specified position with the player's mark
    result_board[action[0]][action[1]] = player_making_move

    return result_board
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # first row - horizontally
    if board[0][0] == X and board[0][1] == X and board[0][2] == X:
        return X
    elif board[0][0] == O and board[0][1] == O and board[0][2] == O:
        return O
    # second row - horizontally
    elif board[1][0] == X and board[1][1] == X and board[1][2] == X:
        return X
    elif board[1][0] == O and board[1][1] == O and board[1][2] == O:
        return O
    # third row - horizontally
    elif board[2][0] == X and board[2][1] == X and board[2][2] == X:
        return X
    elif board[2][0] == O and board[2][1] == O and board[2][2] == O:
        return O
    # first row - vertically
    elif board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return X
    elif board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return O
    # second row - vertically
    elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return X
    elif board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return O
    # third row - vertically
    elif board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return X
    elif board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return O
    # diagonal -1
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    # diagonal -2
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    else:
        return None


def is_tile_empty(board, row, col):
    """
    Checks if a single tile on the Tic Tac Toe board is empty.
    
    Args:
        board (list): The Tic Tac Toe board (2D list).
        row (int): The row index of the tile.
        col (int): The column index of the tile.
        
    Returns:
        bool: True if the tile is empty, False otherwise.
    """

    return board[row][col] == ''


def terminal(board):
    """ 
    Returns True if game is over, False otherwise.
    """

    # Check if there's a winner
    if winner(board=board) == X or winner(board=board) == O:
        return True  # If there's a winner, the game is over

    # Check if any tile is empty
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return False  # If any tile is empty, the game is not over

    # If there are no empty tiles and no winner, it's a tie game
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    while terminal(board=board):
        if winner(board=board) == X:
            return 1
        elif winner(board=board) == O:
            return -1
        elif winner(board=board) == None:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check if the game is over
    if terminal(board):
        return None  # Return None if the game is over
    else:
        # Determine the current player
        if player(board) == X:
            # If the current player is X, find the maximum value move
            value, move = max_value(board, float('-inf'), float('inf'))
            return move
        else:
            # If the current player is O, find the minimum value move
            value, move = min_value(board, float('-inf'), float('inf'))
            return move


def max_value(board, alpha, beta):
    """
    Returns the maximum value and the corresponding move for the current player on the board.
    """
    # Check if the game is over
    if terminal(board):
        return utility(board), None  # Return the utility value if the game is over

    v = float('-inf')  # Initialize v as negative infinity
    move = None

    # Iterate through all possible actions
    for action in actions(board):
        aux, act = min_value(result(board, action), alpha, beta)  # Get the minimum value and corresponding move
        if aux > v:
            v = aux
            move = action
            if v == 1:  # If a winning move is found, return it immediately
                return v, move

        # Update alpha value
        alpha = max(alpha, v)

        # Perform alpha-beta pruning
        if v >= beta:
            break

    return v, move


def min_value(board, alpha, beta):
    """
    Returns the minimum value and the corresponding move for the current player on the board.
    """
    # Check if the game is over
    if terminal(board):
        return utility(board), None  # Return the utility value if the game is over

    v = float('inf')  # Initialize v as positive infinity
    move = None

    # Iterate through all possible actions
    for action in actions(board):
        aux, act = max_value(result(board, action), alpha, beta)  # Get the maximum value and corresponding move
        if aux < v:
            v = aux
            move = action
            if v == -1:  # If a losing move is found, return it immediately
                return v, move

        # Update beta value
        beta = min(beta, v)

        # Perform alpha-beta pruning
        if v <= alpha:
            break

    return v, move
