# 
class AboutClassAttributes(unittest.TestCase):
    class Dog:
        """I am a dog without a name."""
        bionomal_name = "Canine"

    def test_defining_functions_on_individual_objects(self):
        fido = self.Dog()
        fido.bark = lambda x : 'bark ' + x

        self.assertEqual(__, fido.bark("I like swimming"))