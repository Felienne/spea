# 
class Puppy:
    def give_food(self, food):
        return "Yum, I like {0}".format(food)

class AboutClasses(unittest.TestCase):

    def test_methods_can_take_parameters(self):
        fluffy = Puppy()
        self.assertEqual("Yum, I like potatoes", fluffy.give_food(__))