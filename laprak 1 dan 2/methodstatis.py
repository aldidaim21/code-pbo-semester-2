class matematika_184220030:
    @staticmethod
    def tambah(a, b):
        return a + b

    @staticmethod
    def kurang(a, b):
        return a - b

    @staticmethod
    def kali(a, b):
        return a*b

    @staticmethod
    def bagi(a, b):
        return a/b

    @staticmethod
    def bagi_int(a, b):
        return a // b

    @staticmethod
    def sisabagi(a, b):
        return a % b

    @staticmethod
    def pangkat(a, b):
        return a ** b


# pemanggilan langsung

# panggil tambah
print(matematika_184220030.tambah(10, 2))

# panggil kurang
print(matematika_184220030.kurang(11, 12))

# pemanggilan objek
tambah1 = matematika_184220030()
print(tambah1.tambah(10, 1))
