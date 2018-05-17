# 
class AboutAssignments(unittest.TestCase):
    class PossessiveSetter(object):
        def __setattr__(self, attr_name, value):
            new_attr_name =  attr_name

            if attr_name == 'comic':
                new_attr_name = "my_" + new_attr_name
            if attr_name == 'pie':
                new_attr_name = "a_" + new_attr_name

            object.__setattr__(self, new_attr_name, value)

    def test_setattr_intercepts_attribute_assignments(self):
        fanboy = self.PossessiveSetter()

        fanboy.pie = 'blueberry'

        self.assertEqual(__, fanboy.a_pie)
        self.assertEqual(__, fanboy.pie)