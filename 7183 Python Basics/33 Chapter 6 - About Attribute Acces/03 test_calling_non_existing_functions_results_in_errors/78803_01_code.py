# 
class AboutAssignments(unittest.TestCase):
    class Panda:
        bionomal_name = "Ailuropoda melanoleuca"
        colors = ["black", "white"]

        def __init__(self, name):
            self.name = name

        def number_of_paws(self):
            return 4

    def test_calling_non_existing_functions_results_in_errors(self):
        xing_ya = self.Panda("Xing Ya")
        with self.assertRaises(___): xing_ya.number_of_wings()