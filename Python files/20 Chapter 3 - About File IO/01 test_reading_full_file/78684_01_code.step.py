# 
class AboutFileIO(unittest.TestCase):

    def test_reading_full_file(self):
        the_file = open("one_line.txt")
        contents = the_file.read()

        self.assertEqual(__, contents)