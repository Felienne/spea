# 
class AboutPrintingClasses(unittest.TestCase):

    def test_all_objects_support_str_and_repr(self):
        seq = [1, 2, 3]

        self.assertEqual(__, str(seq))
        self.assertEqual(__, repr(seq))

        self.assertEqual(__, str("STRING"))
        self.assertEqual(__, repr("STRING"))