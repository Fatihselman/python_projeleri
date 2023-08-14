import random

def main():
    zar = [1, 2, 3, 4, 5, 6]
    return random.choice(zar)

istek = input("Zar atıp sonucunu denemek ister misiniz? (yes/no): ")

if istek == "yes":
    print("Zar attınız! Sonuç:", main())
elif istek == "no":
    print("Hadi yürü git o zaman")
else:
    print("Niye buradasın bir de yanlış seçiyorsun")

