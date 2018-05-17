# 
class Cat:
    def __init__(self, n):
        self.name = n

    def what_am_I(self):
        return self        

class AboutClasses(unittest.TestCase):

    def test_init_method_can_also_take_data(self):
        felix = Cat("Felix Domestica Prima")
        self.assertEqual(__, felix.name)