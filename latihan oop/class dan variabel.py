class hero:
    # class variabel
    jumlah = 0

    def __init__(self, name, power, armor):
        self.name = name
        self.power = power
        self.armor = armor
        hero.jumlah += 1
        print("memuat hero dengan nama "+name)


hero1 = hero("asep", 100, 10)
print(hero.jumlah)
