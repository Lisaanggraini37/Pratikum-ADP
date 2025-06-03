def buat_data_buku():
    data_buku = [
        "9780201729558,Linear Algebra and Its Applications,Gilbert Strang,5,110000,175000",
        "9781292020587,Calculus and Analytic Geometry,George B. Thomas,6,130000,195000",
        "9780134462455,Python Crash Course,Eric Matthes,10,90000,150000",
        "9780134845623,Introduction to Python Programming,Y. Daniel Liang,5,95000,160000",
        "9780321781079,Calculus: Early Transcendentals,James Stewart,7,120000,180000",
        "9780521867443,Geometric Algebra for Physicists,Chris Doran,2,125000,200000",
        "9780262033848,Introduction to Algorithms,Cormen et al.,4,150000,220000",
        "9780073383095,Advanced Engineering Mathematics,Erwin Kreyszig,6,140000,210000",
        "9781108457651,A First Course in Probability,Sheldon Ross,9,100000,160000",
        "9780470458365,Mathematical Methods for Physics and Engineering,K.F. Riley,4,135000,190000"
    ]
    with open('inventaris_buku.txt', 'w') as file:
        for baris in data_buku:
            file.write(baris + '\n')
buat_data_buku()

def buat_baris(baris):
    kolom = []
    kolom_sementara = ''
    for karakter in baris:
        if karakter == ',':
            kolom.append(kolom_sementara)
            kolom_sementara = ''
        elif karakter != '\n':
            kolom_sementara += karakter
    kolom.append(kolom_sementara) 
    return kolom

def baca_data_buku(data_buku):
    buku_list = []
    with open(data_buku, 'r') as file:
        for baris in file:
            data = buat_baris(baris)
            if len(data) == 6:
                buku = {
                    'ISBN': data[0],
                    'Judul': data[1],
                    'Penulis': data[2],
                    'Stok': int(data[3]),
                    'Harga_Beli': int(data[4]),
                    'Harga_Jual': int(data[5])
                }
                buku_list.append(buku)
    return buku_list

def potensi_dan_buat_laporan(buku_list, data_buku_output):
    with open(data_buku_output, 'w') as file:
        file.write("ISBN,Judul Buku,Penulis,Stok,Harga Beli,Harga Jual,Potensi Keuntungan\n")
        for buku in buku_list:
            keuntungan = (buku['Harga_Jual'] - buku['Harga_Beli']) * buku['Stok']
            buku['Potensi_Keuntungan'] = keuntungan
            baris = buku['ISBN'] + ',' + buku['Judul'] + ',' + buku['Penulis'] + ',' + \
                    str(buku['Stok']) + ',' + str(buku['Harga_Beli']) + ',' + \
                    str(buku['Harga_Jual']) + ',' + str(keuntungan) + '\n'
            file.write(baris)

def analisis_inventaris(buku_list):
    if not buku_list:
        print("Data buku kosong.")
        return

    total_nilai = 0
    buku_rendah_stok = []
    buku_untung_max = buku_list[0]
    buku_untung_min = buku_list[0]

    for buku in buku_list:
        potensi = buku['Potensi_Keuntungan']
        total_nilai += buku['Stok'] * buku['Harga_Beli']

        if potensi > buku_untung_max['Potensi_Keuntungan']:
            buku_untung_max = buku
        if potensi < buku_untung_min['Potensi_Keuntungan']:
            buku_untung_min = buku
        if buku['Stok'] < 5:
            buku_rendah_stok.append(buku)

    print("\n >)Buku dengan potensi keuntungan tertinggi:")
    print(f"{buku_untung_max['Judul']} - Rp{buku_untung_max['Potensi_Keuntungan']}")

    print("\n >)Buku dengan potensi keuntungan terendah:")
    print(f"{buku_untung_min['Judul']} - Rp{buku_untung_min['Potensi_Keuntungan']}")

    print(f"\n >)Total nilai inventaris: Rp{total_nilai}")

    print("\n >)Buku dengan stok kurang dari 5:")
    for buku in buku_rendah_stok:
        print(f"- {buku['Judul']} (Stok: {buku['Stok']})")

buku_list = baca_data_buku('inventaris_buku.txt')
potensi_dan_buat_laporan(buku_list, 'laporan_inventaris.txt')
analisis_inventaris(buku_list)
