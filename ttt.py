import copy


class Board(object):

    def __init__(self, board):
        self.board = board
        self.val = 0
        self.children = []

    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val

    def __eq__(self, other):
        return self.board == other.board and self.val == other.val

    def __ne__(self, other):
        return self.board != other.board or self.val != other.val

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __str__(self):
        res = ''
        print('  ' + str(['0', '1', '2']))
        for index, row in enumerate(self.board):
            res += str(index) + ' ' + str(row) + '\n'
        return res


def game_over(board):

    winning = {
        'XXX': 1,
        'OOO': -1
    }

    # check for player 1 winning
    for index, row in enumerate(board):
        for k, v in winning.iteritems():

            # check horizontal
            if ''.join(row) == k:
                return True, v

            if board[0][index] + board[1][index] + board[2][index] == k:
                    return True, v

            if index == 0:
                # check top-left to bottom-right diagonal
                if row[0] + board[1][1] + board[2][2] == k:
                    return True, v
                # check top-right to bottom-left diagonal
                if row[2] + board[1][1] + board[2][0] == k:
                    return True, v

    # check for a non-complete game
    for row in board:
        for spot in row:
            if spot == ' ':
                return False, 0

    # all spots are filled, but no one won - so it's a tie
    return True, 0


def get_all_moves(player, board):
    boards = []
    symbol = ' '
    if player == 1:  # x's
        symbol = 'X'
    else:
        symbol = 'O'
    for o_index, row in enumerate(board):
        for i_index, spot in enumerate(row):
            if spot == ' ':
                cpy_board = copy.deepcopy(board)
                cpy_board[o_index][i_index] = symbol
                boards.append(Board(cpy_board))
    return boards


def build_game_tree(player, board):
    won, tmp = game_over(board.board)
    board.val = tmp
    if won:
        return board
    children = get_all_moves(player, board.board)
    for child in children:
        child = build_game_tree(abs(3 - player), child)
        board.children.append(child)
    if player == 1:
        board.val = max(board.children).val
    else:
        board.val = min(board.children).val
    return board


def print_optimal_path(board):
    best = max(board.children)
    print('')
    print(best.val)
    print(str(best))
    if len(best.children) > 0:
        print_optimal_path(best)


if __name__ == '__main__':
    def check_game(board):
        won, p = game_over(board.board)
        if won:
            if p == 0:
                print('It\'s a tie!')
            elif p == 1:
                print('The computer won!')
            else:
                print('You won!')
        return won

    mat_board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    print('starting game...')
    while True:
        b = Board(mat_board)
        print(str(b))
        if check_game(b):
            break
        b = build_game_tree(1, b)
        b = max(b.children)
        print(str(b))
        won, p = game_over(b.board)
        if check_game(b):
            break
        coord = map(int, raw_input('Enter the coordinates of where you\'d like to play\n').split())
        mat_board = b.board
        mat_board[coord[1]][coord[0]] = 'O'
