# 
=


class AboutPartialApplication(unittest.TestCase):
    def maximum(self, a, b):
        if a > b:
            return a
        else:
            return b

    def test_partial_function_applied_regularly(self):
        max = functools.partial(self.maximum)

        self.assertEqual(__, max(7, 23))
        self.assertEqual(__, max(10, -10))