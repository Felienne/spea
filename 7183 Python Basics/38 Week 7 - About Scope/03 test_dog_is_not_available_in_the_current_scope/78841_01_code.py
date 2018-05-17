# 
class AboutScope(unittest.TestCase):

    def test_dog_is_not_available_in_the_current_scope(self):
        with self.assertRaises(___): fido = Dog()