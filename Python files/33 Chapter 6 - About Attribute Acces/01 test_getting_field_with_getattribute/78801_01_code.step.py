# 
class AboutAssignments(unittest.TestCase):
    class Panda:
        bionomal_name = "Ailuropoda melanoleuca"
        colors = ["black", "white"]

        def __init__(self, name):
            self.name = name

        def number_of_paws(self):
            return 4

    def test_getting_field_with_getattribute(self):
        wu_wen = self.Panda("Wu Wen")
        name = wu_wen.__getattribute__('name')
        self.assertEqual(__, name)