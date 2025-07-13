def kalimat(text):
    lebar_layar = 80
    jumlah_kalimat = len(text)
    rata_kiri = (lebar_layar - jumlah_kalimat) // 2
    rata_kanan = (lebar_layar - jumlah_kalimat - rata_kiri)
    rata_kiri_str = " " * rata_kiri
    rata_kanan_str = " " * rata_kanan
    rata_tengah = rata_kiri_str + text + rata_kanan_str
    return rata_tengah


text = "Selamat datang di PEMROGRAMAN ANALISA DATA"
rata_tengah = kalimat(text)
print(rata_tengah)



    
