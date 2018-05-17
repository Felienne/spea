# 
class AboutPartialApplication(unittest.TestCase):
    def maximum(self, a, b):
        if a > b:
            return a
        else:
            return b

    def test_partial_that_wrappers_all_args(self):
        always_99 = functools.partial(self.maximum, 99, 20)
        always_20 = functools.partial(self.maximum, 9, 20)

        self.assertEqual(__, always_99())
        self.assertEqual(__, always_20())