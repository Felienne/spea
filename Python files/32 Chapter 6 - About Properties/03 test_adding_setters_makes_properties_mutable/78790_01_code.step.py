# 
class AboutAssignments(unittest.TestCase):
    class MutablePerson:
        def __init__(self):
            self._age = 10

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, value):
            self._age = value

    def test_adding_setters_makes_properties_mutable(self):
        the_flash = self.MutablePerson()
        self.assertEqual(_____, the_flash.age)
        the_flash.age = 24
        self.assertEqual(______, the_flash.age)