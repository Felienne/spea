# 
class FancyCat:
    def __init__(self, n, t):
        self.name = n
        self.title = t

    def get_full_name(self):
        return "{0}. {1}".format(__,self.name)

class AboutClasses(unittest.TestCase):

    def test_different_objects_have_different_instance_variables(self):
        magically_evil_cat = FancyCat("Norris", "Mrs")
        evil_cat = FancyCat("Bigglesworth", "Mr")

        self.assertEqual(__, magically_evil_cat.title)
        self.assertEqual(__, evil_cat.name)