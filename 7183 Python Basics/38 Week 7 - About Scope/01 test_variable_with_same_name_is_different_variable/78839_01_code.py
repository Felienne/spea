# 
counter = 0 # Global

class AboutScope(unittest.TestCase):

    def test_variable_with_same_name_is_different_variable(self):
        counter = 12
        self.assertEqual(__, counter)