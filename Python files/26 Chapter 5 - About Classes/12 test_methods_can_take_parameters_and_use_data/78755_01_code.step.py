# 
class Kitten:
    def __init__(self, favorite_food):
        self.favorite_food = favorite_food

    def give_food(self, food):
        if food == self.favorite_food:
            return "Yum!"
        else:
            return "Uuuuuuugh!"

class AboutClasses(unittest.TestCase):

    def test_methods_can_take_parameters_and_use_data(self):
        garfield = Kitten("lasagna")
        self.assertEqual(__, garfield.give_food("potatoes"))
        self.assertEqual("Yum!", garfield.give_food(__))