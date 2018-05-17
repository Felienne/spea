# 
class AboutAssignments(unittest.TestCase):
    class Dada:
        def __init__(self):
            self._names_are_meaningless = "Oote oote oote"

        @property
        def poetry(self):
            return self._names_are_meaningless


        @poetry.setter
        def poetry(self,value):
            self._names_are_meaningless = value

    def test_matching_properties_and_fields_are_used_by_convention_only(self):
        dada = self.Dada()
        self.assertEqual(__, dada.poetry)
        dada.__ = "Boe"
        self.assertEqual("Boe", dada.poetry)
        self.assertEqual(__, dada._names_are_meaningless)