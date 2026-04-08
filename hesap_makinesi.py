#basit hesap makinesi
sayi1 = float(input("İlk sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# acik kaynak kodlu bir hesap makinesi örneği
# acik kaynak kodlu bir hesap makinesi örneği 2

print("işlemler")
print("1:toplama")
print("2:çıkarma")
print("3:çarpma")
print("4:bölme")
print("5:üs alma")

islem = input("bir işlem seçin: ")

if (islem == "1"):
    sonuç = sayi1 + sayi2
    print(sonuç)
elif (islem == "2"):
    sonuç = sayi1 - sayi2
    print(sonuç)
elif (islem == "3"):
    sonuç = sayi1 * sayi2
    print(sonuç)
elif (islem == "4"):
    sonuç = sayi1 / sayi2
    if (sayi2 != 0):
        print(sonuç)
    else:
        print("error:number is zero")
elif (islem == "5"):
    sonuc = sayi1 ** sayi2
    print(sonuc)

else:
    print("geçersiz sayılar")