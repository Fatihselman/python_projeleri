import random

def main():
    return random.randint(1,6)

istek = input("Zar atıp sonucunu görmek ister misiniz? (yes/no): ")

if istek == "yes":
    zar_sonuc = main()
    print("Zar attınız! Sonuç:", " ".join(["*" if i == zar_sonuc else "." for i in range(1, 7)]))
elif istek == "no":
    print("Hadi yürü git o zaman")
else:
    print("Niye buradasın bir de yanlış seçiyorsun")
