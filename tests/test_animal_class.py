import unittest
from animal import Animal

class Test_animal(unittest.Testcase):
    
    def test_animal_cat(self):
        checkcat = Animal()

        if checkcat.type == 'cat':
            self.assertEqual(checkcat.name, 'Seymour')

    def test_animal_dog(self):
        checkdog = Animal()

        if checkdog.type == 'dog':
            self.assertEqual(checkdog.name, 'Seymour')

    def test_animal_name(self):
        checkname = Animal()

        if checkname.name == name:
            self.assertEqual(checkname.name, name)

    def test_animal_cat_size(self):
        checksize = Animal()

        if checksize.type == 'cat':
            if checksize.size == 'small':
                print('meow')
            else:
                print('MEOW!')

    def test_animal_dog_size(self):
        checksize = Animal()

        if checksize.type == 'dog':
            if checksize.size == 'small':
                print('bow wow')
            elif checksize.size == 'medium':
                print('Ruff ruff')
            else:
                print('arf arf')

    def test_animal_age(self):
        checkage = Animal()

        if checkage.age < 10:
            return