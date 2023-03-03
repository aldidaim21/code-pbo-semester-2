class jajargenjang_184220030:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def ubahAlas(self, alas):
        self.alas = alas

    def ubahTinggi(self, tinggi):
        self.tinggi = tinggi

    def hitungLuas(self):
        return self.alas * self.tinggi

    def tambahKeliling(self):
        self.alas + self.tinggi

    def hitungKeliling(self):
        return self.tambahKeliling()*2

    def cetakLuas(self):
        print('Luas jajargenjang =%.2f' % self.hitungLuas)

    def cetakKeliling(self):
        print('Kelilig persigi panjang =%.2f' % self.hitungKeliling())
