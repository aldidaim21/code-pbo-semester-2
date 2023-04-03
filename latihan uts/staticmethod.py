class menu():

    jumlah_menu = 0

    def __init__(self, nama, asal, peminat):
        self.nama = nama
        self.asal = asal
        self.peminat = peminat
        menu.jumlah_menu += 1

    def banyakmenu(self):
        print('banyaknya menu', menu.jumlah_menu)

    def detail_menu(self):
        print('nama pelanggan', self.nama)
        print('nama asal', self.asal)
        print('peminat', self.peminat)


obj1 = menu('rendang', 'padang', 'banyak')
obj2 = menu('babi georek', 'bali', 'dikit')

# objek
obj1.detail_menu()
obj2.detail_menu()
menu.banyakmenu(menu)
