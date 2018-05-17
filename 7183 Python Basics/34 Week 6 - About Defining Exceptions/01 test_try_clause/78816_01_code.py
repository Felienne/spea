# 
class AboutAssignments(unittest.TestCase):
    class MySpecialError(RuntimeError):
        pass

    def test_try_clause(self):
        result = None
        try:
            self.fail("Oops")
        except Exception as ex:
            result = 'exception handled'
            stored_exception = ex

        self.assertEqual(__, result)

        self.assertEqual(__, isinstance(stored_exception, Exception))
        self.assertEqual(__, isinstance(stored_exception, RuntimeError))

        self.assertTrue(issubclass(RuntimeError, __))

        self.assertEqual(__, stored_exception.args[0])