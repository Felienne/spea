# 
counter = 0 # Global

class AboutScope(unittest.TestCase):

    def test_global_access_is_possible_with_keyword(self):
        global counter
        self.assertEqual(__, counter)