class StringList_184220030(list):
    def __init__(self):
        self.data = []

    def __repr__(self):
        return str(self.data)

    # override methode dari append()
    def append(self, objek):
        if not isinstance(objek, str):
            raise TypeError('objek harus tipe string')
        self.data.append(objek)

    def insert(self, index, objek):
        if index >= len(self.data) or \
                index < - len(self.data):
            raise IndexError('index di luar rentang')
        if not isinstance(objek, str):
            # override metode append()
            raise TypeError('Objek harus bertipe string')
        self.data.insert(index, objek)


# membuat objeknya
slist = StringList_184220030()
# menambah data menggunakan metode append()
slist.append('Python')
slist.append('Ruby')
slist.append('PHP')
print(slist)

# menambah data menggunakan metode insert()
slist.insert(2, 'Perl')
print(slist)
# output ['Python', 'Ruby', 'Perl', 'PHP']
slist.insert(-3, 'Java')
print(slist)

# # erorr
# slist.append(99)

#insert erorr diluar panjangindex
slist.insert(900, "asep")
