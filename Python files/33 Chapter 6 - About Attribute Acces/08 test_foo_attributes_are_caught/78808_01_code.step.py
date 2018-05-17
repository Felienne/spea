# 
class AboutAssignments(unittest.TestCase):
    class WellBehavedFooCatcher:
        def __getattribute__(self, attr_name):
            if attr_name[:3] == "foo":
                return "Foo to you too"
            else:
                return super().__getattribute__(attr_name)

    def test_foo_attributes_are_caught(self):
        catcher = self.WellBehavedFooCatcher()

        self.assertEqual(__, catcher.foo_bar)
        self.assertEqual(__, catcher.foo_baz)