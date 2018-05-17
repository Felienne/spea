# 
class AboutAssignments(unittest.TestCase):
    class Cat:
        @property
        def name(self):
            return self._name

        @name.setter
        def name(self,value):
            if value.lower() == "cat":
                raise ValueError("cats deserve a proper name")
            elif value.lower() == "dog":
                raise TypeError("what is wrong with you?!")
            else:
                self._name = value

    def test_validation_reject_invalid_values(self):
        bob = self.Cat()
        with self.assertRaises(ValueError):
            bob.name = __

        bob = self.Cat()
        with self.assertRaises(___):
            bob.name = "dog"