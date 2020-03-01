import unittest
from TicTacToeChecker import tictactoechecker

class MyTestCase(unittest.TestCase):
    def test_number_of_zeros(self):
        board = [[0, 0, 1],
                 [0, 1, 2],
                 [2, 1, 0]]
        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.number_of_zeros_on(board), 4)

    def test_1_won_with_board(self):
        board =  [[1, 1, 1],
                    [0, 2, 2],
                    [0, 0, 0]]

        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.check_who_won(board), 1)

    def test_1_won_with_given_board_2(self):
        board = [[1, 2, 1],
                 [1, 2, 2],
                 [1, 0, 0]]

        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.check_who_won(board), 1)


    def test_2_won_with_given_board(self):
        board =  [[0, 1, 1],
                    [2, 2, 2],
                    [0, 0, 0]]

        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.check_who_won(board), 2)


    def test_2_won_with_given_board_2(self):
        board =  [[2, 1, 1],
                    [2, 1, 2],
                    [2, 0, 0]]

        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.check_who_won(board), 2)

    def test_draw_won_with_given_board(self):
        board = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]

        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.check_who_won(board), 0)

    def test_unsolved_board(self):
        board = [[0, 0, 1],
                 [0, 1, 2],
                 [2, 1, 0]]

        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.is_solved(board), -1)

    def test_winner_is_1(self):
        board = [[1, 1, 1],
                 [0, 0, 2],
                 [2, 1, 1]]

        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.is_solved(board), 1)

    def test_winner_is_2(self):
        board = [[1, 0, 1],
                 [0, 0, 2],
                 [2, 2, 2]]

        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.is_solved(board), 2)

    def test_winner_is_1(self):
        board = [[1, 0, 1],
                 [0, 1, 2],
                 [2, 2, 1]]

        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.is_solved(board), 1)

    def test_draw(self):
        board = [[1, 2, 1],
                 [1, 1, 2],
                 [2, 1, 2]]

        t = tictactoechecker.TicTacToeChecker()
        self.assertEqual(t.is_solved(board), 0)





if __name__ == '__main__':
    unittest.main()
