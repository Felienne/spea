# 
def add(a, b):
    return a + b

class AboutHigherOrderFunctions(unittest.TestCase):

    def test_assigning_functions_to_variables(self):
        plus = add
        self.assertEqual(__, plus(5,7))