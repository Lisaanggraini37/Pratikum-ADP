while True:
    baris_A = int(input("Masukkan jumlah baris matriks A = "))
    kolom_A = int(input("Masukkan jumlah kolom matriks A = "))
    baris_B = int(input("Masukkan jumlah baris matriks B = "))
    kolom_B = int(input("Masukkan jumlah kolom matriks B = "))
    print("Elemen Matriks A :")
    A=[]
    for i in range(baris_A):
        row=[]
        for j in range(kolom_A):
            elemen=int(input(f"A[{i}][{j}]="))
            row.append(elemen)
        A.append(row)
    print("Matriks A :")
    for i in range(baris_A):
        print("[", end=" ")
        for j in range(kolom_A):
            print(A[i][j], end=" ")
        print("]")
    print()
    print("Elemen Matriks B :")
    B=[]
    for i in range(baris_B):
        row=[]
        for j in range(kolom_B):  
            elemen=int(input(f"B[{i}][{j}]="))
            row.append(elemen)
        B.append(row)
    print("Matriks B :")
    for i in range(baris_B):
        print("[", end=" ")
        for j in range(kolom_B):
            print(B[i][j], end=" ")
        print("]")

    print("\nMenu Kalkulator Matriks :" \
    "\n1. Penjumlahan Matriks" \
    "\n2. Pengurangan Matriks" \
    "\n3. Perkalian Matriks" \
    "\n4. Determinan Matriks" \
    "\n5. Invers Matriks" \
    "\n6. Transpose Matriks" \
    "\n7. Keluar dari program")
    print()
    pilihan = int(input("Pilih menu (1-6) : "))
    print()

    if pilihan == 1:
        if baris_A != baris_B or kolom_A != kolom_B:
            print("Operasi penjumlahan matriks tidak dapat dilakukan!")
            print()
        else:
            hasil=[]
            for i in range(baris_A):
                row=[]
                for j in range(kolom_A):
                    row.append(A[i][j] + B[i][j])
                hasil.append(row)
            print("Hasil Penjumlahan Matriks A dan Matriks B :")
            for row in hasil:
                print('[', end=' ')
                for elemen in row:
                    print(f"{elemen:^4}", end='')
                print(']')
        print()

    elif pilihan == 2:
        if baris_A != baris_B or kolom_A != kolom_B:
            print("Operasi pengurangan matriks tidak dapat dilakukan!")
            print()
        else:
            hasil=[]
            for i in range(baris_A):
                row=[]
                for j in range(kolom_A):
                    row.append(A[i][j] - B[i][j])
                hasil.append(row)
            print("Hasil Pengurangan Matriks A dan Matriks B :")
            for row in hasil:
                print('[', end=' ')
                for elemen in row:
                    print(f"{elemen:^4}", end='')
                print(']')
        print()

    elif pilihan == 3:
        if kolom_A != baris_B:
            print("Operasi Perkalian Matriks tidak dapat dilakukan!")
            print()
        else:
            hasil = []
            for i in range(baris_A):
                row = []
                for  j in range(kolom_B):
                    total = 0
                    for k in range(kolom_A):
                        total += A[i][k]*B[k][j]
                    row.append(total)
                hasil.append(row)
            print("Hasil Perkalian Matriks A dan Matriks B :")
            for row in hasil:
                print('[', end=' ')
                for total in row:  
                    print(f"{total:^4}", end='')  
                print(']')
        print()

    elif pilihan == 4:
        if baris_A!=kolom_A:
            print("Operasi determinan matriks A tidak bisa dilakukan!")
            print()
        else:
            baru = []
            for row in A:
                baru.append(row[0:])
            n = baris_A
            det_A = 1
            for i in range(n):
                if baru[i][i] == 0:
                    for k in range(i+1, n):
                        if baru[k][i] != 0:
                            t = baru[i]
                            baru[i] = baru[k]
                            baru[k] = t
                            det_A *= -1
                            break
                if baru[i][i] == 0:
                    det_A = 0
                    break
                det_A *= baru[i][i]
                for j in range(i+1, n):
                    rasio = baru[j][i] / baru[i][i]
                    for k in range(n):
                        baru[j][k] -= rasio * baru[i][k]
            print("Determinan Matriks A : ", round(det_A))

        if baris_B!=kolom_B:
            print("Operasi determinan matriks B tidak bisa dilakukan!")
            print()
        else:
            baru = []
            for row in B:
                baru.append(row[0:])
            n = baris_B
            det_B = 1
            for i in range(n):
                if baru[i][i] == 0:
                    for k in range(i+1, n):
                        if baru[k][i] != 0:
                            t = baru[i]
                            baru[i] = baru[k]
                            baru[k] = t
                            det_B *= -1
                            break
                if baru[i][i] == 0:
                    det_B = 0
                    break
                det_B *= baru[i][i]
                for j in range(i+1, n):
                    rasio = baru[j][i] / baru[i][i]
                    for k in range(n):
                        baru[j][k] -= rasio * baru[i][k]
            print("Determinan Matriks B : ", round(det_B))
        print()

    elif pilihan == 5:
        if baris_A != kolom_A:
            print("Operasi invers matriks A tidak bisa dilakukan!")
            print()
        else:
            if baris_A == kolom_A:
                n = baris_A
                baru = []
                for row in A:
                    baru.append(row[0:])
                identitas = []
                for i in range(n):
                    baris = []
                    for j in range(n):
                        if i == j:
                            baris.append(1)
                        else:
                            baris.append(0)
                    identitas.append(baris)
                for i in range(n):                 
                    if baru[i][i] == 0:
                        for k in range(i+1, n):
                            if baru[k][i] != 0:
                                t = baru[i]
                                baru[i] = baru[k]
                                baru[k] = t
                                s = identitas[i]
                                identitas[i] = identitas[k]
                                identitas[k] = s
                                break
                    if baru[i][i] == 0:
                        print("Matriks A tidak memiliki invers (determinan = 0)")
                        break
                    pembagi = baru[i][i]
                    for j in range(n):
                        baru[i][j] /= pembagi
                        identitas[i][j] /= pembagi
                    for k in range(n):
                        if k != i:
                            faktor = baru[k][i]
                            for j in range(n):
                                baru[k][j] -= faktor * baru[i][j]
                                identitas[k][j] -= faktor * identitas[i][j]
                else:
                    print("Invers Matriks A:")
                    for i in range(n):
                        print("[", end=" ")
                        for j in range(n):
                            print(f"{round(identitas[i][j], 1):^5}", end=" ")
                        print("]")

        if baris_B != kolom_B:
            print("Operasi invers matriks B tidak bisa dilakukan!")
            print()
        else:
            if baris_B == kolom_B:
                n = baris_B
                baru = []
                for row in B:
                    baru.append(row[0:])
                identitas = []
                for i in range(n):
                    baris = []
                    for j in range(n):
                        if i == j:
                            baris.append(1)
                        else:
                            baris.append(0)
                    identitas.append(baris)
                for i in range(n):
                    if baru[i][i] == 0:
                        for k in range(i+1, n):
                            if baru[k][i] != 0:
                                t = baru[i]
                                baru[i] = baru[k]
                                baru[k] = t
                                s = identitas[i]
                                identitas[i] = identitas[k]
                                identitas[k] = s
                                break
                    if baru[i][i] == 0:
                        print("Matriks B tidak memiliki invers (determinan = 0)")
                        break
                    pembagi = baru[i][i]
                    for j in range(n):
                        baru[i][j] /= pembagi
                        identitas[i][j] /= pembagi
                    for k in range(n):
                        if k != i:
                            faktor = baru[k][i]
                            for j in range(n):
                                baru[k][j] -= faktor * baru[i][j]
                                identitas[k][j] -= faktor * identitas[i][j]
                else:
                    print("Invers Matriks B:")
                    for i in range(n):
                        print("[", end=" ")
                        for j in range(n):
                            print(f"{round(identitas[i][j], 1):^5}", end=" ")
                        print("]")
        print()

    elif pilihan == 6:
        if baris_A and kolom_A:
            transpose = []
            for j in range(kolom_A):
                row = []
                for i in range(baris_A):
                    row.append(A[i][j])
                transpose.append(row)
            print("\nMatriks Transpose A:")
            for row in transpose:
                print('[', end=' ')
                for matriks in row:
                    print(f"{matriks:^4}", end='')  
                print(']')
        if baris_B and kolom_B:
            transpose = []
            for j in range(kolom_B):
                row = []
                for i in range(baris_B):
                    row.append(B[i][j])
                transpose.append(row)
            print("\nMatriks Transpose B:")
            for row in transpose:
                print('[', end=' ')
                for matriks in row:
                    print(f"{matriks:^4}", end='')  
                print(']')
        print()

    elif pilihan == 7:
        print("Terima kasih, kalkulator matriks  selesai digunakan.")
        print()
        break

    else:
        print("Pilihan tidak valid! Silakan pilih angka 1 sampai 7.")
        print()
        continue
            