class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks


mangaratiba = City('Mangaratiba', 'Brasil', 41.220,
                   'A escravatura foi preponderante na formação econômica e '
                   'social de Mangaratiba. ')

print(vars(mangaratiba))
