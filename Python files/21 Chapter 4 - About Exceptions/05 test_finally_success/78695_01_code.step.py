# 
class AboutExceptions(unittest.TestCase):

    def test_finally_success(self):

        try:
            result = 12 / 3
        except ZeroDivisionError:
            result = "You can't divide by zero, silly."
        finally:
            result = "Nevermind"

        self.assertEqual(__, result)