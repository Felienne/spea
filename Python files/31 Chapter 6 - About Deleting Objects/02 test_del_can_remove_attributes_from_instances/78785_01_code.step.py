# 
class AboutAssignments(unittest.TestCase):
    class Bird:
        def __init__(self):
            self.wings = 2

        def fly(self):
            return "I believe I can fly"

    def test_del_can_remove_attributes_from_instances(self):
        flappy = self.Bird()
        del flappy.wings

        try:
            number_of_wings = flappy.wings
        except AttributeError as e:
            error_message = e.args[0]

        self.assertEqual(error_message, __)

        polly = self.Bird()
        number_of_wings = polly.wings

        self.assertEqual(number_of_wings, __)