# 
def format_info(name, age = 18):
   """This returns the passed info as a nicely formatted string"""
   name_and_age_formatted = "{0} is currently {1} years old".format(name,age)

   return name_and_age_formatted

class AboutFunctions(unittest.TestCase):
    def test_calling_with_default_values(self):
        self.assertEqual(__, format_info('Arnold', 70))
        self.assertEqual(__, format_info('Elle'))