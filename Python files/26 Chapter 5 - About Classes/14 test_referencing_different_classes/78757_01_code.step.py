# 
class Puppy:
    def give_food(self, food):
        return "Yum, I like {0}".format(food)

class AboutClasses(unittest.TestCase):

    class Puppy:
        def give_food(self, food):
            return "More {0} please".format(food)

    def test_referencing_different_classes(self):
        beethoven = Puppy()
        fang = self.Puppy()

        self.assertEqual("Yum, I like shoes", beethoven.give_food(__))
        self.assertEqual(__, fang.give_food("shoes"))