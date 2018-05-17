# 
class AI:
    def is_self_aware(self):
        return AI == type(self)

class AboutClasses(unittest.TestCase):

    def test_self_aware(self):
        alexa = AI()
        self.assertEqual(__, alexa.is_self_aware())