import unittest

from app import create_app


class WebAppTests(unittest.TestCase):
    def setUp(self):
        self.client = create_app(
            {"TESTING": True, "SECRET_KEY": "test-secret"}
        ).test_client()

    def test_home_shows_empty_board_and_first_player(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Turno del giocatore <strong>X</strong>", response.text)
        self.assertEqual(response.text.count('name="position"'), 9)

    def test_moves_are_played_and_winner_is_shown(self):
        for position in (1, 4, 2, 5, 3):
            response = self.client.post("/move", data={"position": position})
            self.assertEqual(response.status_code, 302)

        response = self.client.get("/")

        self.assertIn("Ha vinto il giocatore X!", response.text)
        self.assertEqual(response.text.count("class=\"cell\""), 9)
        self.assertEqual(response.text.count("\n              disabled"), 9)

    def test_invalid_move_shows_message(self):
        self.client.post("/move", data={"position": 0})

        response = self.client.get("/")

        self.assertIn("Casella non valida o già occupata.", response.text)

    def test_reset_starts_a_new_game(self):
        self.client.post("/move", data={"position": 1})
        self.client.post("/reset")

        response = self.client.get("/")

        self.assertIn("Turno del giocatore <strong>X</strong>", response.text)
        self.assertIn('value="1"', response.text)


if __name__ == "__main__":
    unittest.main()
