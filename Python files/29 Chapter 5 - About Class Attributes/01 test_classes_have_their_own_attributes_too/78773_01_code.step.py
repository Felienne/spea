# 
class AboutClassAttributes(unittest.TestCase):

    class Dog:
        """I am a dog without a name."""
        bionomal_name = "Canine"

    def test_classes_have_their_own_attributes_too(self):
        fido = self.Dog()
        self.assertEqual(__, fido.bionomal_name)