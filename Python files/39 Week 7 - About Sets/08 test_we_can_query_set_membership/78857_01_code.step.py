# 
class AboutSets(unittest.TestCase):

    def test_we_can_query_set_membership(self):
        beatles = {'John', 'Ringo', 'George', 'Paul'}
        one_direction = {"Harry", "Niall", "Louis", "Liam", "Zayn"}

        self.assertEqual(__, 'John' in beatles )
        self.assertEqual(__, 'Ringo' not in one_direction)