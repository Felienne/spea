# 
class AboutSets(unittest.TestCase):

    def test_we_can_compare_subsets(self):

        beatles = {'John', 'Ringo', 'George', 'Paul'}
        dead_musicians = {'John', 'George', 'Elvis', 'Tupac', 'Bowie'}

        dead_beatles = beatles & dead_musicians

        self.assertEqual(__, dead_beatles <= beatles)
        self.assertEqual(__, dead_beatles.issubset(beatles) )