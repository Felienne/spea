# 
def add(a, b):
    return a + b

def multiply_by_adding(a, b):
    total = 0
    for i in range(b):
        total = add(a, total)
    return total

class AboutAssignments(unittest.TestCase):
    def test_functions_can_call_each_other(self):
        self.assertEqual(__, multiply_by_adding(5,3))