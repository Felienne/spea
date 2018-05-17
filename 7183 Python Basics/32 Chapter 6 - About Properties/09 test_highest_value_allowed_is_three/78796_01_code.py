# 
class AboutAssignments(unittest.TestCase):
    class TicTacToe:
        def __init__(self):
            self._x = 0
            self._y = 0

        @property
        def y(self):
            return self._y

        @y.setter
        def y(self, value):
            __

    def test_highest_value_allowed_is_three(self):
        game = self.TicTacToe()
        game.y = 2
        self.assertEqual(2,game.y)
        game.y = 4
        self.assertEqual(3,game.y)
        # hint: you need to write the setter