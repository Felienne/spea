# 
def format_info(name, age = 18):
   """This returns the passed info as a nicely formatted string"""
   name_and_age_formatted = "{0} is currently {1} years old".format(name,age) 

class AboutFunctions(unittest.TestCase):
    def test_function_too_can_have_documentation(self):
        self.assertEqual(__, format_info.__doc__)