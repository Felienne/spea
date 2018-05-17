# 
class AboutExceptions(unittest.TestCase):

    def test_assert_is_raised(self):
        with self.assertRaises(__):
            result = 12 / 0