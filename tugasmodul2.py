print("                                                        ")
print("               SELAMAT DATANG DI E-TIKET                ")
print("                                                        ")
print("========================================================")
print("|                 DAFTAR KODE MASKAPAI                 |")
print("|Kode|Tujuan Maskapai| Ekonomi  |  Bisnis  |First class|")
print("|3012|Padang-Jakarta |Rp.800.000|Rp.850.000|Rp.900.000 |")
print("|4015|Padang-Batam   |Rp.500.000|Rp.550.000|Rp.700.000 |")
print("|4050|Padang-Bandung |Rp.700.000|Rp.800.000|Rp.850.000 |")
print("========================================================")
print("                                                        ")
print("----------------BELI TIKET >3 DISKON 20%----------------")
print("                                                        ")
print("                STRUK PEMESANAN TIKET                   ")
print("                                                        ")
nama=input("1. Nama             = ")
umur=int(input("2. Umur             = "))
jenis_kelamin=input("3. Jenis kelamin    = ")
print("--------------------------------------------------------")
kode_maskapai=int(input("4. Kode maskapai    = "))
if kode_maskapai==3012:
    print("   ~Tujuan maskapai = Padang-Jakarta")
    kelas=input("5. Kelas maskapai   = ")
    jumlah_tiket=int(input("6. Jumlah tiket     = "))
    if kelas=="ekonomi":
        harga_tiket=800000 
    elif kelas=="bisnis":
        harga_tiket=850000    
    elif kelas=="first class":
        harga_tiket=900000
    if jumlah_tiket>3:
        diskon=harga_tiket*jumlah_tiket*20/100
        harga_total=(harga_tiket*jumlah_tiket)-diskon
        print("7. Harga Total      = Rp.", str(round(harga_total)))
    else:
        harga_total=harga_tiket*jumlah_tiket
        print("7. Harga Total      = Rp.", str(round(harga_total)))

elif kode_maskapai==4015:
    print("   ~Tujuan maskapai = Padang-Batam")
    kelas=input("5. Kelas maskapai   = ")
    jumlah_tiket=int(input("6. Jumlah tiket     = "))
    if kelas=="ekonomi":
        harga_tiket=500000        
    elif kelas=="bisnis":
        harga_tiket=550000       
    elif kelas=="first class":
        harga_tiket=700000 
    if jumlah_tiket>3:
        diskon=harga_tiket*jumlah_tiket*20/100
        harga_total=(harga_tiket*jumlah_tiket)-diskon
        print("7. Harga Total      = Rp.", str(round(harga_total)))
    else:
        harga_total=harga_tiket*jumlah_tiket
        print("7. Harga Total      = Rp.", str(round(harga_total)))

elif kode_maskapai==4050:
    print("   ~Tujuan maskapai = Padang-Bandung")
    kelas=input("5. Kelas maskapai   = ")
    jumlah_tiket=int(input("6. Jumlah tiket     = "))
    if kelas=="ekonomi":
        harga_tiket=700000        
    elif kelas=="bisnis":
        harga_tiket=800000        
    elif kelas=="first class":
        harga_tiket=850000
    if jumlah_tiket>3:
        diskon=harga_tiket*jumlah_tiket*20/100
        harga_total=(harga_tiket*jumlah_tiket)-diskon
        print("7. Harga Total      = Rp.", str(round(harga_total)))
    else:
        harga_total=harga_tiket*jumlah_tiket
        print("7. Harga Total      = Rp.", str(round(harga_total)))
        
else:
    print("-------------Kode maskapai tidak ditemukan--------------")
    print("------------------SILAHKAN COBA LAGI--------------------")
print("                                                        ")
print("-----------------------THANK YOU------------------------")
print("                                                        ")