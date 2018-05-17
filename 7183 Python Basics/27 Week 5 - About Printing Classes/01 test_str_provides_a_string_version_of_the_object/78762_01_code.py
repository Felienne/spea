# 
class AboutPrintingClasses(unittest.TestCase):
    class PrintableDog:
        def __init__(self, initial_name):
            self._name = initial_name

        def __str__(self):
            #
            # Implement this!
            #
            return __

        def __repr__(self):
            return "A dog named '" + self._name + "'"

    def test_str_provides_a_string_version_of_the_object(self):
        sue = self.PrintableDog("Sue")

        self.assertEqual("Sue", str(sue))