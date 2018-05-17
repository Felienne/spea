# 
class AboutFileIO(unittest.TestCase):

    def test_reading_file_with_for_strip(self):
        the_file = open("short_lines.txt")

        lines = list()

        for line in the_file:
            line = line.strip()
            lines.append(line)

        self.assertEqual(__, lines)