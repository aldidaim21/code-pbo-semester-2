    # membuat class bangun ruang belah ketupat
    class balok_184220040:
        # atribut statis
        penghitung = 0

        def __init__(self, panjang, lebar, tinggi):
            balok_184220040.penghitung += 1
            # atribut bukan statis
            self.panjang = panjang
            self.lebar = lebar
            self.tinggi = tinggi

        def ubahPanjang(self, panjang):
            self.panjang = panjang

        def ubahLebar(self, lebar):
            self.lebar = lebar

        def ubahTinggi(self, tinggi):
            self.tinggi = tinggi

        def hitungLuas(self):
            return self.panjang * self.lebar * self.tinggi

        def hitungKeliling(self):
            return 4*(self.panjang + self.lebar + self.tinggi)

        def cetakLuas(self):
            print('Luas Balok = %.2f' % self.hitungLuas(), 'cm')

        def cetakKeliling(self):
            print('Luas keliling balok = %.2f' % self.hitungKeliling(), 'cm')


    # objek
    objek1 = balok_184220040(10, 10, 10)
    objek2 = balok_184220040(10, 10, 10)

    # cetak luas
    objek1.cetakLuas()
    objek2.cetakLuas()
    objek1.cetakKeliling()

    # counter
    print(balok_184220040.penghitung)
    print(objek1.penghitung)
    print(objek2.penghitung)
