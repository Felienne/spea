# 
class Bird:
    def __init__(self):
        self.age = 1 

class AboutClasses(unittest.TestCase):

    def test_init_is_a_special_method(self):
        tweety = Bird()
        self.assertEqual(__, tweety.age)