# 
class Dog:
    """Dogs need regular walks. Never, ever let them drive."""
    age = 1

    def age_in_dog_years(self):
        return self.age * 7

class AboutClasses(unittest.TestCase):

    def test_instances_of_classes_can_be_created_with_parentheses(self):
        fido = Dog()
        self.assertEqual(Dog, _________(fido))