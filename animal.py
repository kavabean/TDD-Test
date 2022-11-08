
class Animal:
    def __init__(self, type):
        self.type = type
        self.size = ''
        self.age = 0
        self.name = self.get_name()

    def speak(self):
        print('here')
        if self.size == 'small':
            if self.type == 'cat':
                result = 'meow'
            elif self.type == 'dog':
                result = 'bow wow'
            else:
                pass
        elif self.size == 'medium':
            if self.type == 'cat':
                result = 'MEOW!'
            elif self.type == 'dog':
                result = 'Ruff ruff'
            else:
                pass
        elif self.size != '':
            if self.type == 'dog':
                result = 'arf arf'
        else:
            result = 'New animal discovered'
        
        return(result)

    def describe(self):

        if self.age < 10:
            return(f'{self.name} is young')
        elif self.age >= 10:
            return(f'{self.name} is old')


    def get_name(self):
        if self.type == 'cat':
            return 'Seymour'
        elif self.type == 'dog':
            return 'Spot'

    def animal_calib(self, type, name, age, size):
        self.name = name
        self.age = age
        self.size = size
        self.type = type

        self.get_name()
