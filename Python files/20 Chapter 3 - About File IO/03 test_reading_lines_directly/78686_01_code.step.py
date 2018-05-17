# 
class AboutFileIO(unittest.TestCase):

    def test_reading_lines_directly(self):
        the_file = open("short_lines.txt")

        lines = the_file.readlines()

        self.assertEqual(__, lines)