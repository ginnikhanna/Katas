class TicTacToeChecker:
    def __init__(self):
        pass

    def number_of_zeros_on(self, board):
        return sum(x.count(0) for x in board)

    def check_for_unsolved_board(self, board):
        if self.number_of_zeros_on(board) != 0:
            return True

    def did_number_win(self, board, number):
        if board[0][0] == board[1][1] == board[2][2] == number:
            return True

        for list in board:
            i = 0
            if list[i] == list[i + 1] == list[i + 2] == number:
                return True

        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == number:
                return True

    def check_who_won(self, board):
        if self.did_number_win(board, 1):
            return 1
        if self.did_number_win(board, 2):
            return 2

        return 0

    def is_solved(self, board):
        if self.check_who_won(board) == 1 or self.check_who_won(board) == 2:
           return self.check_who_won(board)
        if self.check_for_unsolved_board(board):
           return -1

        return 0

