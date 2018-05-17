# 
class AboutAssignments(unittest.TestCase):
    class Counter:
        def __init__(self):
            self._count = 0

        @property
        def count(self):
            self._count += _____
            return self._count

    def test_properties_allow_calculation(self):
        graaf_tel = self.Counter()
        self.assertEqual(1, graaf_tel.count)
        self.assertEqual(2, graaf_tel.count)
        self.assertEqual(3, graaf_tel.count)