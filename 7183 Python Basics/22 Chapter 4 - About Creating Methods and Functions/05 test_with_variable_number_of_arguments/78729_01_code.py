# 
def print_all_these(*args):
    to_print = ""
    for a in args:
        to_print += a + " "
    return to_print


class AboutFunctions(unittest.TestCase):
    def test_with_variable_number_of_arguments(self):
        self.assertEqual(__, print_all_these('Huey'))
        self.assertEqual(__, print_all_these('Huey','Dewey'))
        self.assertEqual(__, print_all_these('Huey','Dewey','Louie'))