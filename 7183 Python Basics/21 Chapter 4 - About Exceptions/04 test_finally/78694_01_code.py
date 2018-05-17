# 
class AboutExceptions(unittest.TestCase):

    def test_finally(self):

        try:
            result = 12 / 0
        except ZeroDivisionError:
            result = "You can't divide by zero, silly."
        finally:
            result = "Nevermind"

        self.assertEqual(__, result)