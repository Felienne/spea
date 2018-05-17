# 
class AboutExceptions(unittest.TestCase):

    def test_catch_problems(self):

        try:
            result = 12 / 0
        except Exception:
            result = "You can't divide by zero, silly."

        self.assertEqual(__, result)