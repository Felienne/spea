# 
class Calculator:
    total = 0

    def add(self, value):
        self.total += value
        return self

class AboutClasses(unittest.TestCase):

    def test_type_of_return_self_is(self):
        c = Calculator()

        self.assertEqual(Calculator, _________(c.add(1)))