# 
class AboutInheritance(unittest.TestCase):

    class Dog:
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

        def bark(self):
            return "WOOF"

    def test_dogs_are_still_dogs(self):
        boef = self.Dog('Boef')
        self.assertEqual(self.Dog, __)