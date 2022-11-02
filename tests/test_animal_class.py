from cgitb import small
import unittest
from animal import Animal

class Test_animal(unittest.TestCase):

    def test_name_cat(self):
        checkcat = Animal('cat')

        pass

        self.assertEqual(checkcat.name, 'Seymour')

    def test_name_dog(self):
        checkdog = Animal('dog')
        
        pass
            
        self.assertEqual(checkdog.name, 'Spot')

    def test_animal_name(self):
        checkname = Animal()
        name = Animal(name)
        
        pass

        self.assertEqual(checkname.name, name)

    def test_animal_cat_size(self):
        checksize1 = Animal('cat')
        checksize1.size = 'small'

        self.speak1 = checksize1.speak()

        self.assertEqual(self.speak1, 'meow')


        checksize2 = Animal('cat')
        checksize2.size = 'small'

        self.speak2 = Animal.speak()

        self.assertEqual(self.speak2, 'meow')

    def test_animal_dog_size(self):
        checksize1 = Animal('dog')
        checksize1.size = 'small'

        self.speak1 = checksize1.speak()

        self.assertEqual(self.speak1, 'bow wow')


        checksize2 = Animal('dog')
        checksize2.size = 'medium'

        self.speak2 = Animal.speak()

        self.assertEqual(self.speak2, 'Ruff ruff')


        checksize3 = Animal('dog')
        checksize3.size = not 'medium' or 'small'

        self.speak3 = Animal.speak()

        self.assertEqual(self.speak3, 'arf arf')

    def test_animal_age(self):
        checkage1 = Animal(self.age)
        checkage1 < 10
        
        self.age1 = Animal.describe()

        self.assertEqual(self.age1, f'{checkage1} is young')

        checkage2 = Animal(self.age)
        checkage2 >= 10
        
        self.age2 = Animal.describe()

        self.assertEqual(self.age2, f'{checkage2} is old')
