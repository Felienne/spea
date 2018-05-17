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

    class Chihuahua(Dog):
        def wag(self):
            return "happy"

    def test_but_what_are_chihuahuas(self):
        tinkerbell = self.Chihuahua('Tinkerbell')
        self.assertEqual(__, type(tinkerbell))