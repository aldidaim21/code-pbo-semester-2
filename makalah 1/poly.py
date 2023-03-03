# fungsi yang dapat diterapkan pada berbagai jenis objek
def print_details(obj):
    print("Tipe objek:", type(obj))
    print("Panjang objek:", len(obj))
    print("Isi objek:", obj)


# pemanggilan fungsi dengan tipe data yang berbeda
print_details("Hello, World!")
print_details([1, 2, 3, 4, 5])
print_details({"nama": "Andi", "usia": 25})
