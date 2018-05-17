# 
class AboutAssignments(unittest.TestCase):
    class Panda:
        bionomal_name = "Ailuropoda melanoleuca"
        colors = ["black", "white"]

        def __init__(self, name):
            self.name = name

        def number_of_paws(self):
            return 4

    def test_calling_getattribute_causes_an_attribute_error(self):
        typical = self.Panda("Melan")

        with self.assertRaises(___): typical.____getattribute____('foobar')

        # THINK ABOUT IT:
        #
        # If the method __getattribute__() causes the AttributeError, then
        # what would happen if we redefine __getattribute__()?