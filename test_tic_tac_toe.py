import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from tic_tac_toe import create_board, get_winner, is_draw, main, make_move


class TicTacToeTests(unittest.TestCase):
    def test_detects_rows_columns_and_diagonals(self):
        winning_boards = (
            ["X", "X", "X", " ", "O", " ", " ", " ", "O"],
            ["O", "X", " ", "O", "X", " ", "O", " ", "X"],
            ["X", "O", " ", "O", "X", " ", " ", " ", "X"],
            [" ", " ", "O", "X", "O", " ", "O", "X", "X"],
        )
        for board in winning_boards:
            with self.subTest(board=board):
                self.assertEqual(get_winner(board), "X" if board[0] == "X" else "O")

    def test_detects_draw(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertIsNone(get_winner(board))
        self.assertTrue(is_draw(board))

    def test_move_rejects_out_of_range_occupied_and_invalid_player(self):
        board = create_board()
        self.assertFalse(make_move(board, 0, "X"))
        self.assertFalse(make_move(board, 10, "X"))
        self.assertFalse(make_move(board, 1, "Y"))
        self.assertTrue(make_move(board, 1, "X"))
        self.assertFalse(make_move(board, 1, "O"))
        self.assertEqual(board[0], "X")

    def test_game_retries_invalid_and_occupied_cells(self):
        inputs = iter(("abc", "0", "1", "1", "4", "2", "5", "3"))
        output = io.StringIO()
        with patch("builtins.input", side_effect=lambda _prompt: next(inputs)):
            with redirect_stdout(output):
                main()
        self.assertIn("Inserisci un numero da 1 a 9.", output.getvalue())
        self.assertIn("Casella non valida o già occupata.", output.getvalue())
        self.assertIn("Ha vinto il giocatore X!", output.getvalue())


if __name__ == "__main__":
    unittest.main()
