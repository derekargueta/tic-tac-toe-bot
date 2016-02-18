import unittest
from ttt import get_all_moves

class TestGenerateMoves(unittest.TestCase):

    def test_one(self):
        test_case = [
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', ' ', 'X']
        ]
        one_expected = [
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', 'X', 'X']
        ]
        moves = get_all_moves(1, test_case)
        self.assertEqual(1, len(moves))
        self.assertEqual(one_expected, moves[0].board)

        two_expected = [
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', 'O', 'X']
        ]
        moves = get_all_moves(2, test_case)
        self.assertEqual(1, len(moves))
        self.assertEqual(two_expected, moves[0].board)

    def test_two(self):
        test_case = [
            ['X', ' ', 'X'],
            [' ', 'X', 'X'],
            ['X', ' ', 'X']
        ]
        one_expected = [
            [
                ['X', 'X', 'X'],
                [' ', 'X', 'X'],
                ['X', ' ', 'X']
            ],
            [
                ['X', ' ', 'X'],
                ['X', 'X', 'X'],
                ['X', ' ', 'X']
            ],
            [
                ['X', ' ', 'X'],
                [' ', 'X', 'X'],
                ['X', 'X', 'X']
            ]
        ]
        moves = [board.board for board in get_all_moves(1, test_case)]
        self.assertEqual(3, len(moves))
        self.assertTrue(one_expected[0] in moves)
        self.assertTrue(one_expected[1] in moves)
        self.assertTrue(one_expected[2] in moves)

        two_expected = [
            [
                ['X', 'O', 'X'],
                [' ', 'X', 'X'],
                ['X', ' ', 'X']
            ],
            [
                ['X', ' ', 'X'],
                ['O', 'X', 'X'],
                ['X', ' ', 'X']
            ],
            [
                ['X', ' ', 'X'],
                [' ', 'X', 'X'],
                ['X', 'O', 'X']
            ]
        ]
        moves = [board.board for board in get_all_moves(2, test_case)]
        self.assertEqual(3, len(moves))
        self.assertTrue(two_expected[0] in moves)
        self.assertTrue(two_expected[1] in moves)
        self.assertTrue(two_expected[2] in moves)


if __name__ == '__main__':
    unittest.main()
