# 
class AboutScope(unittest.TestCase):
    def inside_local(self):
        msg = "Outside!"

        def inside():
            msg = "Inside!"

        inside()
        return msg

    def test_getting_something_locally(self):
        self.assertEqual(__, self.inside_local())