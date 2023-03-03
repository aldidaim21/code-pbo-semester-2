class persegi_184220030:
    def __init__(self, sisi):
        self.sisi = sisi

    def ubahLuas(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi * self.sisi

    def hitungKeliling(self):
        return 4*self.sisi

    def cetakLuas(self):
        print('Luas persegi= %.2f' % self.hitungLuas())

    def cetakKeliling(self):
        print('Keliling persigi= %.2f' % self.hitungKeliling())


# Membuat objek dari kelas Persegi
persegi1 = persegi_184220030(10)
persegi2 = persegi_184220030(20)

# memanggil objek dari kelas Persegi
persegi1.cetakLuas()
persegi1.cetakKeliling()
print(persegi1)

persegi2.cetakLuas()
persegi2.cetakKeliling()
print(persegi2)
