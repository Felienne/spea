# 
class AboutPartialApplication(unittest.TestCase):
    def maximum(self, a, b):
        if a > b:
            return a
        else:
            return b

    def test_partial__passing_first_arg(self):
        max_with_0 = functools.partial(self.maximum, 0)

        self.assertEqual(__, max_with_0(-4))
        self.assertEqual(__, max_with_0(5))