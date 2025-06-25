import os
import time
from termcolor import colored, cprint

mata_kuliah = []
data_mahasiswa = []

os.system('cls')

def angka(s):
    if len(s) == 0:
        return False
    for i in s:
        if i < '0' or i > '9':
            return False
    return True

def konversi_ipk(nilai):
    if nilai >= 80:
        return 4.00, "A"
    elif nilai >= 75:
        return 3.75, "A-"
    elif nilai >= 70:
        return 3.50, "B+"
    elif nilai >= 65:
        return 3.00, "B"
    elif nilai >= 60:
        return 2.75, "B-"
    elif nilai >= 55:
        return 2.50, "C+"
    elif nilai >= 50:
        return 2.00, "C"
    elif nilai >= 45:
        return 1.00, "D"
    else:
        return 0.00, "E"

def input_mata_kuliah():
    while True:
        jumlah_input = input("Masukkan jumlah mata kuliah: ")
        if angka(jumlah_input) and int(jumlah_input) > 0:
            jumlah = int(jumlah_input)
            break
        else:
            print(colored("Input harus berupa angka lebih dari 0!", "red"))

    for i in range(1, jumlah + 1):
        while True:
            nama = input(f"Masukkan nama mata kuliah ke-{i}: ")
            if nama == "":
                print(colored("Nama mata kuliah tidak boleh kosong!", "red"))
            else:
                break
        while True:
            sks_input = input(f"Masukkan jumlah SKS untuk {nama}: ")
            if angka(sks_input) and int(sks_input) > 0:
                mata_kuliah.append({"nama": nama, "sks": int(sks_input)})
                break
            else:
                print(colored("SKS harus berupa angka dan lebih dari 0!", "red"))

def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    nilai_mahasiswa = []
    for j in mata_kuliah:
        while True:
            nilai_input = input(f"Masukkan nilai {j['nama']} (0-100): ")
            if angka(nilai_input):
                nilai = int(nilai_input)
                nilai_mahasiswa.append(nilai)
                break
            print(colored("Input tidak valid. Harus angka 0-100.", "red"))
    data_mahasiswa.append({"nama": nama, "nilai": nilai_mahasiswa})
    print(colored("Data berhasil ditambahkan!", "green"))

def hitung_ipk_dengan_sks(nilai_list):
    total_bobot = 0
    total_sks = 0
    for i in range(len(mata_kuliah)):
        nilai = nilai_list[i]
        sks = mata_kuliah[i]["sks"]
        ipk_satuan, predikat = konversi_ipk(nilai)
        total_bobot += ipk_satuan * sks
        total_sks += sks
    return total_bobot / total_sks

def tampilkan_berjalan(teks, delay=0.02):
    for karakter in teks:
        print(karakter, end="", flush=True)
        time.sleep(delay)

def tampilkan_data():
    if not data_mahasiswa:
        print(colored("Belum ada data mahasiswa.", "red"))
        return
    rata_mahasiswa = []
    for mahasiswa in data_mahasiswa:
        total = 0
        for n in mahasiswa["nilai"]:
            total += n
        rata = total / len(mahasiswa["nilai"])
        rata_mahasiswa.append(rata)
    nilai_tertinggi = max(rata_mahasiswa)
    nilai_terendah = min(rata_mahasiswa)
    header = "\n" + "=" * (30 + len(mata_kuliah)*17 + 13 + 12) + "\n"
    header += f"|{'Nama':^24} | "
    for k in mata_kuliah:
        nama_matkul = f"{k['nama']} ({k['sks']} sks)"
        header += f"{nama_matkul:^15} | "
    header += f"{'Rata-rata':^9} | {'Predikat':^8} |\n"
    header += "-" * (30 + len(mata_kuliah)*17 + 13 + 12) + "\n"
    tampilkan_berjalan(header)

    for i in range(len(data_mahasiswa)):
        mahasiswa = data_mahasiswa[i]
        rata = rata_mahasiswa[i]
        ipk_satuan, predikat = konversi_ipk(rata)
        warna = "white"
        if rata == nilai_tertinggi:
            warna = "green"
        elif rata == nilai_terendah:
            warna = "red"
        nama_warna = colored(mahasiswa["nama"], warna)
        baris = f"|{nama_warna:^33} | "
        for nilai in mahasiswa["nilai"]:
            baris += f"{nilai:^15} | "
        baris += f"{rata:^9.2f} | {predikat:^7} |\n"
        tampilkan_berjalan(baris)
    garis = "=" * (30 + len(mata_kuliah)*17 + 13 + 12) + "\n"
    tampilkan_berjalan(garis)

def animasi_ipk(ipk):
    ipk_str = f"{ipk:.2f}"
    print(colored("\nMenampilkan IPK", "yellow", attrs=["bold"]))
    panjang_baris = 30
    durasi = 2
    langkah = 0.05
    total_iterasi = int(durasi / langkah)
    for i in range(total_iterasi + 1):
        progress = i / total_iterasi
        isi = int(panjang_baris * progress)
        bar = "[" + "=" * isi + " " * (panjang_baris - isi) + "]"
        print(f"\r{bar} {progress*100:.0f}%", end="", flush=True)
        time.sleep(langkah)
    print()
    cprint(f"IPK Anda : {ipk_str}", "black", "on_magenta", attrs=["bold"])
    time.sleep(1)

def tampilkan_ipk():
    if not data_mahasiswa:
        print(colored("Belum ada data mahasiswa.", "red"))
        return
    nama_dicari = input("Masukkan nama mahasiswa untuk melihat IPK: ")
    ditemukan = False
    for mahasiswa in data_mahasiswa:
        if mahasiswa["nama"] == nama_dicari:
            ipk_final = hitung_ipk_dengan_sks(mahasiswa["nilai"])
            animasi_ipk(ipk_final)
            ditemukan = True
            break
    if not ditemukan:
        print(colored("Mahasiswa tidak ditemukan.", "red"))

def simpan_ke_file():
    with open("data.txt", "w") as f:
        f.write("=== DATA MATA KULIAH ===\n")
        for i in mata_kuliah:
            f.write(f"{i['nama']} - {i['sks']} SKS\n")

        f.write("\n=== DATA MAHASISWA ===\n")
        for mahasiswa in data_mahasiswa:
            f.write(f"Nama: {mahasiswa['nama']}\n")
            total = 0
            for i in range(len(mahasiswa["nilai"])):
                pel = mata_kuliah[i]
                nilai = mahasiswa["nilai"][i]
                f.write(f"  {pel['nama']} ({pel['sks']} SKS): {nilai}\n")
                total += nilai
            rata = total / len(mahasiswa["nilai"])
            ipk_satuan, predikat = konversi_ipk(rata)
            ipk_final = hitung_ipk_dengan_sks(mahasiswa["nilai"])
            f.write(f"  Rata-rata: {rata:.2f}\n")
            f.write(f"  Predikat: {predikat}\n")
            f.write(f"  IPK: {ipk_final:.2f}\n")
            f.write("-" * 30 + "\n")
    print(colored("Data berhasil disimpan ke file 'data.txt'", "green"))

print("=== Input Mata Kuliah dan SKS ===")
input_mata_kuliah()

while True:
    print("\n=== MENU UTAMA ===")
    print("1. Tambah Mahaiswa")
    print("2. Tampilkan Nilai")
    print("3. Tampilkan IPK Mahaiswa")
    print("4. Simpan ke File")
    print("5. Keluar")
    menu = input("Pilih: ")
    if menu == "1":
        tambah_data()
    elif menu == "2":
        tampilkan_data()
    elif menu == "3":
        tampilkan_ipk()
    elif menu == "4":
        simpan_ke_file()
    elif menu == "5":
        break
    else:
        print(colored("Pilihan tidak valid.", "red"))