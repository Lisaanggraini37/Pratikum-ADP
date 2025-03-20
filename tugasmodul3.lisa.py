print("[-----Menghitung Nilai Variabel Acak Poisson-----]")
print("")
m=int(input("Batas nilai n (M)  = "))
lambda_t=float(input("Nilai lambda(t)    = ")) 
e=2.71828
faktorial=1
print("")
print(f"Nilai P(N(t)=n) dari n=0 sampai n={m} adalah : ")
for n in range(m+1):
    P=e**(-lambda_t)*(lambda_t**n)/faktorial
    faktorial*=n+1
    print(f"{n+1}. (P(N(t)={n}))={P}")