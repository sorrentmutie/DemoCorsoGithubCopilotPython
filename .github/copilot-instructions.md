# Copilot instructions

## Project overview

This repository contains a two-player tic-tac-toe game with both a Flask web
interface and the original terminal interface. `tic_tac_toe.py` owns the
framework-independent game rules and terminal loop; `app.py` exposes those
rules through browser routes, and `templates/index.html` renders the board.
`test_tic_tac_toe.py` covers the rules and terminal game, while `test_app.py`
covers the Flask routes with the built-in test client.

The board is a flat nine-element list in row-major order. Empty cells contain
`" "`, player marks are `"X"` and `"O"`, and user positions are one-based
(`1`-`9`) while internal indexes are zero-based. `_WINNING_LINES` is the
single source of truth for rows, columns, and diagonals.

## Commands

Install dependencies in a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the web app:

```powershell
python app.py
```

Run the terminal version:

```powershell
python tic_tac_toe.py
```

Run the complete test suite:

```powershell
python -m unittest -v
```

Run one test:

```powershell
python -m unittest -v test_app.WebAppTests.test_moves_are_played_and_winner_is_shown
```

No separate formatter, linter, or build command is defined in the repository.

## Implementation conventions

- Keep rule logic in small, directly testable functions (`create_board`,
  `make_move`, `get_winner`, and `is_draw`) and reuse it from both interfaces.
- The Flask app stores the flat board and current player in the browser session;
  `/` renders the game, `/move` handles a turn, and `/reset` starts a new game.
- Keep terminal interaction in `tic_tac_toe.main`; do not move web concerns into
  the rule module.
- Invalid input is handled in the interactive loop: non-integer input prints
  an error and retries, while invalid or occupied positions are rejected by
  `make_move` and also retry.
- `make_move` validates both the player mark and the inclusive position range
  before changing the board. It returns a boolean rather than raising for
  invalid moves.
- Winner and draw checks must not mutate the board. A draw requires no winner
  and every cell to be occupied.
- Preserve the current user-facing Italian messages and board rendering unless
  the behavior is intentionally being changed and the tests are updated.
- Add rule and terminal behavior tests in `test_tic_tac_toe.py`; use
  `unittest.mock.patch` for scripted input and `redirect_stdout` when asserting
  terminal output.
- Add web behavior tests in `test_app.py` using `create_app({"TESTING": True})`
  and Flask's test client; assert redirects and rendered response text rather
  than starting a real server.
