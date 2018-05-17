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

    def test_all_built_in_classes_ultimately_inherit_from_object_class(self):
        self.assertEqual(__, issubclass(str, object))