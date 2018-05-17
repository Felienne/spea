# 
def greet_closure(name):
    def get_message():
        return "Hello there {0}!".format(name)

    return get_message()

class AboutHigherOrderFunctions(unittest.TestCase):

    def test_inner_functions_have_access_to_outer_scope(self):
        self.assertEqual(__, greet_closure("Rose"))