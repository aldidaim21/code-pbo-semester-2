class identitas_kota:
    def __init__(self, kota, kecamatan):
        self.kota = kota
        self.kecamatan = kecamatan

    def informasi_kota(self):
        print('kota', self.kota, 'kecamatanya adalah', self.kecamatan)


class identitaskota1(identitas_kota):
    def informasi_kota(self):
        print('kota', self.kota, 'kecamatan', self.kecamatan)


obj1 = identitas_kota('Bekasi', 'pademangan')
obj2 = identitaskota1('cimahi', 'cibabat')
obj3 = identitaskota1('bandung', 'sariasih')

obj1.informasi_kota()
obj2.informasi_kota()
