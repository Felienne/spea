# 
class AboutAssignments(unittest.TestCase):
    class Bird:
        def __init__(self):
            self.wings = 2

        def fly(self):
            return "I believe I can fly"

    def test_del_can_remove_methods(self):
        flappy = self.Bird()
        polly = self.Bird()

        del self.Bird.fly

        try:
            still_available = flappy.fly()
        except AttributeError as e:
            error_message_flappy = e.args[0]
        self.assertEqual(error_message_flappy, __)

        try:
            still_available = polly.fly()
        except AttributeError as e:
            error_message_polly = e.args[0]
        self.assertEqual(error_message_polly, __)