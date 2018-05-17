# 
class AboutExceptions(unittest.TestCase):

    def test_types_of_exceptions(self):

        try:
            the_file = open("spoon.txt")
        except ZeroDivisionError as ex:
            result = "You found a division error!"

        except IOError as ex:
            result = "There is no spoon"

        self.assertEqual(__, result)