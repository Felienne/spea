# 
class Dog:
    """Dogs need regular walks. Never, ever let them drive."""
    age = 1

    def age_in_dog_years(self):
        return self.age * 7


class AboutClasses(unittest.TestCase):

    def test_objects_have_methods(self):
        fido = Dog()
        self.assertEqual(__, fido.age_in_dog_years())