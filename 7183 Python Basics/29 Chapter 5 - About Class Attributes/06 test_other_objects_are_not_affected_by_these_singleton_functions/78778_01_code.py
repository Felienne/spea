# 
class AboutClassAttributes(unittest.TestCase):
    class Dog:
        """I am a dog without a name."""
        bionomal_name = "Canine"

    def test_other_objects_are_not_affected_by_these_singleton_functions(self):
        fido = self.Dog()
        fido.bark = lambda x : 'bark ' + x

        self.assertEqual(__, fido.bark("I like swimming"))

        rover = self.Dog()

        with self.assertRaises(___): rover.wag()