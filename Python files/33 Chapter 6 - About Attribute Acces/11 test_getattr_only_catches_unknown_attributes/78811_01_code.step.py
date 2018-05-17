# 
class AboutAssignments(unittest.TestCase):
    class MinimalCatcher:
        class DuffObject: pass

        def __init__(self):
            self.no_of_getattr_calls = 0

        def __getattr__(self, attr_name):
            self.no_of_getattr_calls += 1
            return self.DuffObject

        def my_method(self):
            pass

    def test_getattr_only_catches_unknown_attributes(self):
        catcher = self.MinimalCatcher()
        catcher.purple_flamingos()
        catcher.free_pie()

        self.assertEqual(__,
            type(catcher.give_me_duff_or_give_me_death()).__name__)

        self.assertEqual(__, catcher.no_of_getattr_calls)