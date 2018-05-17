# 
class AboutFileIO(unittest.TestCase):

    def test_reading_file_line_by_line(self):
        the_file = open("short_lines.txt")

        a_line = the_file.readline()
        self.assertEqual(__, a_line)

        another_line = the_file.readline()
        self.assertEqual(__, another_line)

        one_more = the_file.readline()
        self.assertEqual(__, one_more)