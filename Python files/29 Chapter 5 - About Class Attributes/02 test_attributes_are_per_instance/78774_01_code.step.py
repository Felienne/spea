# 
class AboutClassAttributes(unittest.TestCase):
    class Dog:
        """I am a dog without a name."""
        bionomal_name = "Canine"

    def test_attributes_are_per_instance(self):
        fido = self.Dog()   
        fluffy = self.Dog()
        self.assertEqual(_____, fido.bionomal_name == fluffy.bionomal_name)
        fido.bionomal_name = "Dogum"
        self.assertEqual(______, fido.bionomal_name == fluffy.bionomal_name)