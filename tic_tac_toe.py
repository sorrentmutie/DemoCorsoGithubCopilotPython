"""Gioco del tris per due giocatori da terminale."""

_WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def create_board():
    return [" "] * 9


def make_move(board, position, player):
    if player not in ("X", "O") or not 1 <= position <= 9:
        return False
    index = position - 1
    if board[index] != " ":
        return False
    board[index] = player
    return True


def get_winner(board):
    for line in _WINNING_LINES:
        first, second, third = (board[index] for index in line)
        if first != " " and first == second == third:
            return first
    return None


def is_draw(board):
    return get_winner(board) is None and all(cell != " " for cell in board)


def print_board(board):
    cells = [cell if cell != " " else str(index + 1) for index, cell in enumerate(board)]
    for row in range(3):
        start = row * 3
        print(f" {cells[start]} | {cells[start + 1]} | {cells[start + 2]} ")
        if row < 2:
            print("---+---+---")


def main():
    board = create_board()
    current_player = "X"

    while True:
        print_board(board)
        try:
            position = int(input(f"Giocatore {current_player}, scegli una casella (1-9): "))
        except ValueError:
            print("Inserisci un numero da 1 a 9.")
            continue

        if not make_move(board, position, current_player):
            print("Casella non valida o già occupata. Riprova.")
            continue

        winner = get_winner(board)
        if winner:
            print_board(board)
            print(f"Ha vinto il giocatore {winner}!")
            return
        if is_draw(board):
            print_board(board)
            print("Pareggio!")
            return

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
