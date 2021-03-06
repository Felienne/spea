# 
class AboutMultipleInheritance(unittest.TestCase):
    class Nameable:
        def __init__(self):
            self._name = None

        def set_name(self, new_name):
            self._name = new_name

        def here(self):
            return "In Nameable class"

    class Animal:
        def legs(self):
            return 4

        def can_climb_walls(self):
            return False

        def here(self):
            return "In Animal class"

    class Pig(Animal):
        def __init__(self):
            super().__init__()
            self._name = "Jasper"

        @property
        def name(self):
            return self._name

        def speak(self):
            return "OINK"

        def color(self):
            return 'pink'

        def here(self):
            return "In Pig class"

    class Spider(Animal):
        def __init__(self):
            super().__init__()
            self._name = "Boris"

        def can_climb_walls(self):
            return True

        def legs(self):
            return 8

        def color(self):
            return 'black'

        def here(self):
            return "In Spider class"

    class Spiderpig(Pig, Spider, Nameable):
        def __init__(self):
            super(AboutMultipleInheritance.Pig, self).__init__()
            super(AboutMultipleInheritance.Nameable, self).__init__()
            self._name = "Jeff"

        def speak(self):
            return "This looks like a job for Spiderpig!"

        def here(self):
            return "In Spiderpig class"

    #
    # Hierarchy:
    #               Animal
    #              /     \
    #            Pig   Spider  Nameable
    #              \      |      /
    #                 Spiderpig
    #
    # ------------------------------------------------------------------

    def test_confirm_the_mro_controls_the_calling_order(self):
        jeff = self.Spiderpig()
        self.assertRegex(jeff.here(), 'Spiderpig')

        next = super(AboutMultipleInheritance.Spiderpig, jeff)
        self.assertRegex(next.here(), 'Pig')

        next = super(AboutMultipleInheritance.Pig, jeff)
        self.assertRegex(next.here(), __)

        # Hang on a minute?!? That last class name might be a super class of
        # the 'jeff' object, but its hardly a superclass of Pig, is it?
        #
        # To avoid confusion it may help to think of super() as next_mro().