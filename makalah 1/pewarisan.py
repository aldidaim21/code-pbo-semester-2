# parent
class hewan:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

# child


class kucing(hewan):
    def makan(self):
        print("kucing sedang makan")


binatang = kucing("catty", "putih")


# atribut
print(binatang.warna)
binatang.makan()
