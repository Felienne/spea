# 
def greet(name):
    def get_message():
        return "Hello there"

    result = get_message() + " {0}!".format(name)
    return result

class AboutHigherOrderFunctions(unittest.TestCase):

    def test_define_functions_in_other_functions(self):
        self.assertEqual(__, greet("Jack"))