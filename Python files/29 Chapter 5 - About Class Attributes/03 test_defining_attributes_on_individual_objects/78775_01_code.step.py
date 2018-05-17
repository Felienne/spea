# 
class AboutClassAttributes(unittest.TestCase):
    class Dog:
        """I am a dog without a name."""
        bionomal_name = "Canine"

    def test_defining_attributes_on_individual_objects(self):
        fido = self.Dog()
        fido.legs = 4

        self.assertEqual(__, fido.legs)