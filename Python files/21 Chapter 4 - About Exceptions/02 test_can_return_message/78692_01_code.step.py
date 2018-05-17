# 
class AboutExceptions(unittest.TestCase):

    def test_can_return_message(self):

        try:
            result = 12 / 0
        except Exception as ex:
            result = ex.args[0]

        self.assertEqual(__, result)