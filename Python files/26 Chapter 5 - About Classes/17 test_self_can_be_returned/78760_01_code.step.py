# 
class Calculator:
    total = 0

    def add(self, value):
        self.total += value
        return self

class AboutClasses(unittest.TestCase):

    def test_self_can_be_returned(self):
        c = Calculator()
        c.add(1).add(1).add(1)
        self.assertEqual(__, c.total)