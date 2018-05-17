# 
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def apply(f, a, b):
    return f(a,b)

class AboutHigherOrderFunctions(unittest.TestCase):

    def test_functions_can_be_passed_as_parameters(self):
        self.assertEqual(__, add(2,3))
        self.assertEqual(__, apply(add,2,3))    
        self.assertEqual(6, apply(_____,2,3))