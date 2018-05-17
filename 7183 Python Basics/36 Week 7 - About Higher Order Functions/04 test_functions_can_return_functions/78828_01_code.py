# 
def add_constant(x):
    def addx(a):
        return a+x
    return addx

class AboutHigherOrderFunctions(unittest.TestCase):

    def test_functions_can_return_functions(self):
        add5 = add_constant(5)
        self.assertEqual(__, add5(3))