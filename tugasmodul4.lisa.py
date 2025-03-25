print()
print("[======================PEMESANAN TIKET BIOSKOP======================]")
print()
r = 0
c = 0
while r < 4 or c < 4:
    r = int(input("Masukkan jumlah baris kursi bioskop (minimal 4) : "))
    c = int(input("Masukkan jumlah kolom kursi bioskop (minimal 4) : "))
    if r < 4 or c < 4:
        print("Ukuran minimal bioskop adalah 4x4! Silahkan masukkan ulang.")
    else:
        print(f"Ukuran kursi bioskop adalah : {r}x{c}")

pesanan_kursi = " " 

while True:
    print()
    print("Layout Kursi Bioskop :")
    for i in range(r):
        for j in range(c):
            no_kursi = i * c + j + 1
            counter = 0  
            karakter = ""  
            for p in pesanan_kursi:
                if p == " ":
                    if karakter == str(no_kursi):  
                        counter = 1
                        break
                    karakter = ""  
                else:
                    karakter += p  

            if counter == 1:
                print(" X", end="  ")
            else:
                print(no_kursi, end="  ")
        print()
    print()

    nomor = int(input("Masukkan nomor kursi yang ingin dipesan (atau 0 untuk selesai) : "))
    t = r * c
    if nomor == 0:
        print("Terima kasih telah memesan tiket!")
        break
    elif nomor < 1 or nomor > t:
        print("Nomor kursi tidak valid! Masukkan nomor kursi yang tersedia.")
        continue 
    
    counter = 0
    karakter = ""
    for p in pesanan_kursi:
        if p == " ":
            if karakter == str(nomor):
                counter = 1
                break
            karakter = ""  
        else:
            karakter += p

    if counter == 1:
        print("Kursi sudah dipesan! Pilih kursi lain.")
    else:
        pesanan_kursi += str(nomor) + " "  
        print("Kursi", nomor, "berhasil dipesan!")
print()