class hero:  # tamplate
    def __init__(self, name, power, armor):
        self.name = name
        self.power = power
        self.armor = armor


hero1 = hero("asep", 100, 10)

# print setiap element
print(hero1.name)
print(hero1.power)
print(hero1.armor)

# print gabung dan pisah
print(type(hero1))
print(hero1.__dict__)
