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


# membuat list kosong
mylist = []
print(mylist)


# menambahkan objek kubus ke dalam mylist
mylist.append(kubus(10))
print(mylist)
# menambahkan objek balok ke dalam mylist
mylist.append(balok(3, 5, 2))
print(mylist)
# menambahkan objek Tabung ke dalam mylist
mylist.append(tabung(10, 10))
print(mylist)


# menelusuri seluruh elemen mylist,
# kemudian memanggil metode luas ()
# dari setiap objek yang ditelusuri
for obj in mylist:
    if not issubclass(obj.__class__, TigaDimensi_184220030):
        raise TypeError('Objek harus turunan dari class tiga dimensi')
    if isinstance(obj, kubus):
        print('Volume kubus  = ', end='')
    elif isinstance(obj, balok):
        print('Volume Blok = ', end='')
    else:
        print('Volume Tabung = ', end='')
    print(obj.Volume())
