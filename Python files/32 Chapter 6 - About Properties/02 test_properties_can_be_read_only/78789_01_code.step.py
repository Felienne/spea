# 
class AboutAssignments(unittest.TestCase):
    class ImmutablePerson:
        def __init__(self):
            self._age = 10

        @property
        def age(self):
            return self._age

    def test_properties_can_be_read_only(self):
        the_flash = self.ImmutablePerson()
        self.assertEqual(10, the_flash.age)

        with self.assertRaises(___):
            the_flash.age = 24