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

    def test_properties_are_methods_that_can_be_accessed_like_variables(self):
        the_flash = self.MutablePerson()
        self.assertEqual(10, the_flash.age)
        the_flash.age += _____
        self.assertEqual(24, the_flash.age)