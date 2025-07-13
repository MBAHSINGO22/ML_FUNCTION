def input_data():
    value = []
    
    jumlah = int(input("Masukkan banyak data = "))
    i = 0
    while i < jumlah:
        value.append(int(input("Masukkan data = ")))
        i+=1
        if i == jumlah:
            break
    value.sort()
    return value

def hitung_median(angka):

    angka.sort()

    length = len(angka)

    if length % 2 == 0:
        median = (angka[length // 2 - 1] + angka[length // 2]) / 2
    else:
        median = angka[length // 2]
    return median


angka = input_data()
median = hitung_median(angka)
print(f"Nilai median dari data yang diberikan adalah: {median}")
