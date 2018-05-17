# 
class FancyCat:
    def __init__(self, n, t):
        self.name = n
        self.title = t

    def get_full_name(self):
        return "{0}. {1}".format(__,self.name)        

class AboutClasses(unittest.TestCase):

    def test_methods_use_data(self):
        evil_cat = FancyCat("Bigglesworth", "Mr")
        self.assertEqual("Mr. Bigglesworth", evil_cat.get_full_name())
        # Hint: Where is the blank for this Koan?