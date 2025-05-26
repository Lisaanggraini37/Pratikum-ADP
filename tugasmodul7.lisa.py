def input_data():
    n = int(input("Masukkan jumlah mahasiswa : "))
    mahasiswa = []
    for i in range(n):
        print(f"\nMahasiswa ke-{i+1}")
        nama = input("Nama        : ")
        nim = int(input("NIM         : "))
        uts = int(input("Nilai UTS   : "))
        uas = int(input("Nilai UAS   : "))
        tugas = int(input("Nilai Tugas : "))
        nilai_akhir = 0.35 * uts + 0.35 * uas + 0.30 * tugas
        mahasiswa.append([nama, nim, uts, uas, tugas, nilai_akhir])
    return mahasiswa

def main():
    data = input_data()
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][5] < data[j + 1][5]:
                tukar = data[j]
                data[j] = data[j + 1]
                data[j + 1] = tukar
    for i in range(n):
        data[i].append(i + 1)
    
    garis = "+----+-----------------+------------+-----+-----+--------+---------------+------------+"
    print("\n" + garis)
    print("| No | Nama            | NIM        | UTS | UAS | Tugas  | Nilai Akhir   | Peringkat  |")
    print(garis)
    for i in range(n):
        m = data[i]
        print("| {:<2} | {:<15} | {:<10} | {:>3} | {:>3} | {:>6} | {:>13.2f} | {:>10} |".format(
            i + 1, m[0], m[1], m[2], m[3], m[4], m[5], m[6]))
    print(garis)
    
    total_uts = 0
    total_uas = 0
    total_tugas = 0
    total_akhir = 0
    for i in range(n):
        total_uts += data[i][2]
        total_uas += data[i][3]
        total_tugas += data[i][4]
        total_akhir += data[i][5]
    rata_uts = total_uts / n
    rata_uas = total_uas / n
    rata_tugas = total_tugas / n
    rata_akhir = total_akhir / n

    print("| {:<2} | {:<15} | {:<10} | {:>3} | {:>3} | {:>6} | {:>13.2f} | {:>10} |".format(
        "", "RATA-RATA", "", int(rata_uts), int(rata_uas), int(rata_tugas), rata_akhir, ""))
    print(garis)

main()
