# 
def make_order_for(foodtype):
    return lambda qty: str(qty) + " " + foodtype + "s"

class AboutAssignments(unittest.TestCase):
    def test_accessing_lambda_without_assignment(self):
        self.assertEqual(__, make_order_for('spam')(39823))