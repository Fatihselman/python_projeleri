def main(miktar, faiz_oranı, ay):
    return (miktar + (miktar * faiz_oranı)) / ay

miktar = int(input("Lütfen para seçiniz: "))
faiz_oranı = float(input("Lütfen faiz oranını seçiniz: "))
ay = int(input("Lütfen ay seçiniz: "))

sonuc = main(miktar, faiz_oranı, ay)
print("Hesaplama sonucu:", sonuc)
