class orang():

    def __init__(self, nama, umur, berat, tinggi):
        self.nama = nama
        self.umur = umur
        self.berat = berat
        self.tinggi = tinggi

    def detail_orang(self):
        print('Nama:', self.nama)
        print('Umur:', self.umur)
        print('Berat Badan:', self.berat, 'kg')
        print('Tinggi Badan:', self.tinggi, 'cm')


orang1 = orang('asep', 30, 20, 180)


orang1.detail_orang()
