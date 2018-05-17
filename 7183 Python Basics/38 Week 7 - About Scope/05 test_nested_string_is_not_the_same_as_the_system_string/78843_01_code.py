# 
class AboutScope(unittest.TestCase):
    class str:
        """Fake string. So sad!"""

    def test_nested_string_is_not_the_same_as_the_system_string(self):
        self.assertEqual(__, self.str.__doc__)