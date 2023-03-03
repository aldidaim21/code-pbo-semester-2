class Mobil:
    def __init__(self, merk):
        self.__merk = merk

    def tampilkan_merk(self):
        print(f'Merk: {self.__merk}')


jip = Mobil('Jeep')
jip.tampilkan_merk()

# # eror
# print(f'Merk: {jip.__merk}')
