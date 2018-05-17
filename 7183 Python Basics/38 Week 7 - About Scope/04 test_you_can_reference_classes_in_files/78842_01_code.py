# 
# We write the files here so you can see what they contain
f1 = open('jims_animals.py', 'w')
f1.write('''
class Dog:
    def identify(self):
        return "I am Jim's dog"
''')
f1.close()

f2 = open('joes_animals.py', 'w')
f2.write('''
class Dog:
    def identify(self):
        return "I am Joe's dog"
''')
f2.close()

# Now we import what we've just written
import jims_animals
import joes_animals

class AboutScope(unittest.TestCase):

    def test_you_can_reference_classes_in_files(self):
        # Here we use the classes in the modules we just imported
        fido = jims_animals.Dog()
        rover = joes_animals.Dog()

        self.assertEqual(__, fido.identify())
        self.assertEqual(__, rover.identify())

        self.assertEqual(__, type(fido) == type(rover))
        self.assertEqual(__, jims_animals.Dog == joes_animals.Dog)