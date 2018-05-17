# 
class Cat:
    __
    def __init__(self, n):
        self.name = n

    def what_am_I(self):
        return self

class AboutClasses(unittest.TestCase):
    def test_classes_have_documentation_too_two(self):
        self.assertEqual(Cat.__doc__, "Cats can walk themselves. Go away!")
        # Hint: Where is the blank for this Koan?