class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.isCaught = is_caught

    def speak(self):
        print(f'Hello, my friend. My name is {self.name}')


pikachu = Pokemon(25, 'Pikachu', 'Electric', 'So fun!', False)

pikachu.speak()

print(vars(pikachu))
