# 
class AboutPrintingClasses(unittest.TestCase):
    class PrintableDog:
        def __init__(self, initial_name):
            self._name = initial_name

        def __str__(self):
            return self._name

        def __repr__(self):
            return "A dog named '" + self._name + "'"

    def test_repr_provides_a_more_complete_string_version(self):
        sue = self.PrintableDog("Sue")
        self.assertEqual(__, repr(sue))