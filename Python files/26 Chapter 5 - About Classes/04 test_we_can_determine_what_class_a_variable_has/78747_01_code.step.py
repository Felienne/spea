# 
class Dog:
    """Dogs need regular walks. Never, ever let them drive."""
    age = 1

    def age_in_dog_years(self):
        return self.age * 7

class AboutClasses(unittest.TestCase):
    def test_we_can_determine_what_class_a_variable_has(self):
        fido = Dog()
        self.assertEqual(__, isinstance(fido, Dog))
        self.assertEqual(False, isinstance(fido, __))