import os

from flask import Flask, redirect, render_template, request, session, url_for

from tic_tac_toe import create_board, get_winner, is_draw, make_move


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "development-only-secret"),
    )
    if test_config:
        app.config.update(test_config)

    @app.get("/")
    def index():
        board = session.get("board", create_board())
        winner = get_winner(board)
        draw = is_draw(board)
        return render_template(
            "index.html",
            board=board,
            current_player=session.get("current_player", "X"),
            winner=winner,
            draw=draw,
            message=session.pop("message", None),
        )

    @app.post("/move")
    def move():
        board = session.get("board", create_board())
        current_player = session.get("current_player", "X")

        if get_winner(board) or is_draw(board):
            session["message"] = "La partita è terminata. Inizia una nuova partita."
            return redirect(url_for("index"))

        try:
            position = int(request.form.get("position", ""))
        except ValueError:
            position = 0

        if not make_move(board, position, current_player):
            session["message"] = "Casella non valida o già occupata."
        else:
            session["board"] = board
            if get_winner(board) is None and not is_draw(board):
                session["current_player"] = "O" if current_player == "X" else "X"

        return redirect(url_for("index"))

    @app.post("/reset")
    def reset():
        session.clear()
        return redirect(url_for("index"))

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
