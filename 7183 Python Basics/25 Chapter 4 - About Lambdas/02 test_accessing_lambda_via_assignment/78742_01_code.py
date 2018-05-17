# 
def make_order_for(foodtype):
    return lambda qty: str(qty) + " " + foodtype + "s"

class AboutAssignments(unittest.TestCase):
    def test_accessing_lambda_via_assignment(self):

        sausages = make_order_for('sausage')
        eggs = make_order_for('egg')

        self.assertEqual(__, sausages(3))
        self.assertEqual(__, eggs(2))