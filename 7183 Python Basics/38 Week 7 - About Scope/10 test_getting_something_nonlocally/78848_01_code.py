# 
class AboutScope(unittest.TestCase):
    def inside_non_local(self):
        msg = "Outside!"

        def inside():
            nonlocal msg
            msg = "Inside!"

        inside()
        return msg

    def test_getting_something_nonlocally(self):
        self.assertEqual(__, self.inside_non_local())