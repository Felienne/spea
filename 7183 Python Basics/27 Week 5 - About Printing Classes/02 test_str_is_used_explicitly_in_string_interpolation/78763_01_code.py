# 
class AboutPrintingClasses(unittest.TestCase):
    class PrintableDog:
        def __init__(self, initial_name):
            self._name = initial_name

        def __str__(self):
            return self._name

        def __repr__(self):
            return "A dog named '" + self._name + "'"

    def test_str_is_used_explicitly_in_string_interpolation(self):
        sue = self.PrintableDog("Sue")

        self.assertEqual(__, "My name is " + str(sue) + ". How do you do?")