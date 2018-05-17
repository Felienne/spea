# 
class AboutClasses(unittest.TestCase):
    class Turtle:
        def __init__(self, n):
            self.name = n

    def test_classes_may_be_nested(self):
        sheldon = self.Turtle('Sheldon')
        self.assertEqual(__, type(sheldon))