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
        for row in self.board:
            res += str(row) + '\n'
        return res


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def print_board(board):
    for row in board:
        print(row)
    print('')


def game_over(board):
    # check for player 1 winning
    for index, row in enumerate(board):
        if ''.join(row) == 'XXX':
            return True, 1
        if index == 0:
            if row[0] + board[1][0] + board[2][0] == 'XXX':
                return True, 1
            if row[0] + board[1][1] + board[2][2] == 'XXX':
                return True, 1
        if index == 2:
            if row[2] + board[1][1] + board[2][0] == 'XXX':
                return True, 1
        if ''.join(row) == 'OOO':
            return True, -1
        if index == 0:
            if row[0] + board[1][0] + board[2][0] == 'OOO':
                return True, -1
            if row[0] + board[1][1] + board[2][2] == 'OOO':
                return True, -1
        if index == 2:
            if row[2] + board[1][1] + board[2][0] == 'OOO':
                return True, -1

    # check for ties
    for row in board:
        for spot in row:
            if spot == ' ':
                return False, 0
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
                # boards.append(cpy_board)
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


print_board(board)
b = Board(board)
root = build_game_tree(1, b)
# print(root.val)
print(str(max(root.children)))
# print_optimal_path(root)
