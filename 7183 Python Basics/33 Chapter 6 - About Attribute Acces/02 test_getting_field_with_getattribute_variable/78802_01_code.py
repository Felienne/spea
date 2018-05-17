# 
class AboutAssignments(unittest.TestCase):
    class Panda:
        bionomal_name = "Ailuropoda melanoleuca"
        colors = ["black", "white"]

        def __init__(self, name):
            self.name = name

        def number_of_paws(self):
            return 4

    def test_getting_field_with_getattribute_variable(self):
        xing_ya = self.Panda("Xing Ya")
        attribute_to_get = "colors"

        colors = xing_ya.__getattribute__(__)
        self.assertEqual(["black", "white"], colors)