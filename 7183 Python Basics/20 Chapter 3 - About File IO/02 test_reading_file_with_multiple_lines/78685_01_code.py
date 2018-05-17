# 
class AboutFileIO(unittest.TestCase):

    def test_reading_file_with_multiple_lines(self):
        the_file = open("short_lines.txt")

        print(the_file)
        contents = the_file.read()

        self.assertEqual(__, contents)