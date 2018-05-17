# 
def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)

class AboutAssignments(unittest.TestCase):
    def test_functions_can_call_themselves(self):
        self.assertEqual(__, factorial(7))