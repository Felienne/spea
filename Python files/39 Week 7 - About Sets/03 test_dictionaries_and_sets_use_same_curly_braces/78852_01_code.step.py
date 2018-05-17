# 
class AboutSets(unittest.TestCase):

    def test_dictionaries_and_sets_use_same_curly_braces(self):
        self.assertEqual(__, type({1, 2, 3}))
        self.assertEqual(__, type({'one': 1, 'two': 2}))
        self.assertEqual(__, type({}))