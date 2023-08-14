sozluk = {
    "fatih": "Fetheden, açan vs. manasına gelmektedir.",
    "zeynep": "En değerli taş gibimsi bir şey bir sürü manası var.",
    "cemile": "Güzel demektir.",
    "ahmet": "Peygamber efendimizin isimlerinden biridir."
}

a = input("Lütfen aile üyelerimizden ismini öğrenmek istediğiniz kişinin adını yazınız: ")

if a.lower() in sozluk:
    print(f"{a.capitalize()} kelimesinin açıklaması: {sozluk[a.lower()]}")
else:
    print("Bu kelime sözlüğümüzde mevcut değildir.")

    