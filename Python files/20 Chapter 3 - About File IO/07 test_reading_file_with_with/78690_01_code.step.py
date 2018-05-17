# 
class AboutFileIO(unittest.TestCase):

    def test_reading_file_with_with(self):
        # there are a number of reasons for it,
        # but using with is the prefered way of opening a file
        # feel free to read up on that if you are interested!

        with open("short_lines.txt") as file:
            self.assertEqual(__, len(file.readlines()))