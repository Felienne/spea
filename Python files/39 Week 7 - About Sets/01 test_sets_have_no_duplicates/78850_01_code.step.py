# 
class AboutSets(unittest.TestCase):

    def test_sets_have_no_duplicates(self):
        highlanders = ['MacLeod', 'MacLeod', 'Matunas', 'Matunas', 'Matunas', 'Malcolm', 'Malcolm']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual(__, there_can_only_be_only_one)