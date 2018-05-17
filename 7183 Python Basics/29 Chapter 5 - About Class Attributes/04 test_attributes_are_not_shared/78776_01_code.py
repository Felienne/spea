# 
class AboutClassAttributes(unittest.TestCase):
    class Dog:
        """I am a dog without a name."""
        bionomal_name = "Canine"

    def test_attributes_are_not_shared(self):
        fido = self.Dog()
        fido.legs = 4
        fluffy = self.Dog()

        with self.assertRaises(___): fluffy.legs