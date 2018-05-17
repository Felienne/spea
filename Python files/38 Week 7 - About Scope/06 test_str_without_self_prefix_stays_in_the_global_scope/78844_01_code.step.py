# 
class AboutScope(unittest.TestCase):
    class str:
        """Fake string. So sad!"""

    def test_str_without_self_prefix_stays_in_the_global_scope(self):
        self.assertEqual(__, str == type("HI"))