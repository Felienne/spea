# 
class AboutSets(unittest.TestCase):

    def test_set_have_arithmetic_operators(self):
        beatles = {'John', 'Ringo', 'George', 'Paul'}
        dead_musicians = {'John', 'George', 'Elvis', 'Tupac', 'Bowie'}

        great_musicians = beatles | dead_musicians
        self.assertEqual(__, great_musicians)

        living_beatles = beatles - dead_musicians
        self.assertEqual(__, living_beatles)

        dead_beatles = beatles & dead_musicians
        self.assertEqual(__, dead_beatles)