# 
class AboutAssignments(unittest.TestCase):
    class Person:
        def __init__(self):
            self.age = 10

        def drive(self):
            if self.age < 18:
                return  "Too young"
            else:
                return "VROOM VROOM"

    def test_fields_are_mutable(self):
        the_flash = self.Person()
        self.assertEqual("Too young", the_flash.drive())
        the_flash.__ = 24
        self.assertEqual("VROOM VROOM", the_flash.drive())