from abc import ABCMeta, abstractmethod


# kelass abstrak
class TigaDimensi_184220030(metaclass=ABCMeta):
    @abstractmethod
    def Volume(self):
        pass


# kelas kubus turunan dari class tiga dimensi
class kubus(TigaDimensi_184220030):
    def __init__(self, s):
        self.sisi = s

    def Volume(self):
        return self.sisi * self.sisi * self.sisi


# kelas Balok  turunan dari kelas Tiga Dimensi
class balok(TigaDimensi_184220030):
    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t

    def Volume(self):
        return self.panjang * self.lebar * self.tinggi


# kelas tabung turunan dari kelas Tiga dimensi
class tabung(TigaDimensi_184220030):
    def __init__(self, r, t):
        self.jarijari = r
        self.tinggi = t

    def Volume(self):
        return 3.14 * self.jarijari * self.jarijari * self.tinggi


# kelas kerucut turunan dari kelas Tiga dimensi
class kerucut(TigaDimensi_184220030):
    def __init__(self, r, t):
        self.jari = r
        self.tinggi = t

    def Volume(self):
        return 1/3 * 3.14 * self.jari * self.jari * self.tinggi


# # error
# obj = TigaDimensi_184220030()

# print(obj)

# pemanggilan objek dengan kelas turunan
obj1 = balok(1, 1, 1).Volume()
print(obj1)

obj2 = kubus(2).Volume()
print(obj2)

obj3 = kerucut(10, 10).Volume()
print(obj3)
