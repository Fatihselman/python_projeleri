import random

print("Lütfen yazmak istediğiniz kadar seçenek yazdıktan sonra ayrılmak için 1'e basın.")

isimlistesi = []  # Önce isimlistesi adında boş bir liste oluşturun

while True:
    x = input("Lütfen bir isim giriniz: ")

    if x == "1":  # Kullanıcının "1" girdiğini kontrol edin
        break  # Döngüyü sonlandırın

    isimlistesi.append(x)
    print(isimlistesi)

if isimlistesi:  # Eğer isimlistesi boş değilse
    secilen_isim = random.choice(isimlistesi)
    print("Rastgele seçilen isim:", secilen_isim)
else:
    print("Liste boş, rastgele seçim yapılamıyor.")
