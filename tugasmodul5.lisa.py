n = int(input("Jumlah praktikan ADP = "))
siswa=[]
nilai=[]
for i in range(n):
    nama_mahasiswa = str(input("Masukkan Nama Mahasiswa : "))
    nilai_pretest = float(input("Nilai pretes  : "))
    nilai_postest = float(input("Nilai postes  : "))
    nilai_makalah = float(input("Nilai makalah : "))
    nilai_akhir = round((nilai_pretest * 0.4) + (nilai_postest * 0.4) + (nilai_makalah * 0.2), 2)
    siswa.append(nama_mahasiswa)
    nilai.append(nilai_akhir)
print(f"Nama Mahasiswa = {siswa}")
print(f"Nilai Akhir Mahasiswa = {nilai}")
print()
print("              Tabel Nilai Mahasiswa              ")
print("+--------------------------------+--------------+")
print("|         Nama Mahasiswa         |  Nilai Akhir |")
print("+--------------------------------+--------------+")
for i in range(n):
    print(f"|{siswa[i]:^30}  |{nilai[i]:>8}      |")
print("+--------------------------------+--------------+")
print()
total=0
for i in range (n):
    total=total+nilai[i]
rata_rata=round((total/n),2)
print(f"Rata-rata nilai akhir kelas = {rata_rata}")

max=nilai[0]
min=nilai[0]
for i in nilai:
    if i>max:
        max=i
    elif i<min:
        min=i
print(f"Nilai Akhir Tertinggi = {max}")
print(f"Nilai Akhir Terendah = {min}")

print("Mahasiswa dengan Nilai Akhir Tertinggi : ")
for i in range (n):
    if nilai[i]==max:
        print(f"- {siswa[i]}")
print("Mahasiswa dengan Nilai Akhir Terendah : ")
for i in range (n):
    if nilai[i]==min:
        print(f"- {siswa[i]}")
print(f"Daftar Mahasiswa dengan Nilai Akhir di atas rata_rata kelas : ")
for i in range(n):
  if nilai[i]>rata_rata:
        print(f"- {siswa[i]} dengan nilai ({nilai[i]})")