# 
class AboutAssignments(unittest.TestCase):
    class Doctor:
        def __init__(self):
            self._age = 903

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, value):
            if value < self.age:
                pass
                # nice try! you can't get any younger
            else:
                self._age = value

    def test_validation3(self):
        jodie = self.Doctor()
        self.assertEqual(903, jodie.age)
        jodie.age += 9
        self.assertEqual(__, jodie.age)