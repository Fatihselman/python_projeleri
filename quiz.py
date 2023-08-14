sorular = [
    {
        "soru": "Dünyanın en büyük okyanusu hangisidir?",
        "cevap": "Pasifik"
    },
    {
        "soru": "Python programlama dili hangi yıl geliştirilmiştir?",
        "cevap": "1989"
    },
    {
        "soru": "Mona Lisa tablosunun ressamı kimdir?",
        "cevap": "Leonardo da Vinci"
    }
]

dogru_sayisi = 0
toplam_soru = len(sorular)

print("Quiz Programına Hoş Geldiniz!")

for soru in sorular:
    print("\n" + soru['soru'])
    cevap = input("Cevabınızı girin: ")

    if cevap.lower() == soru['cevap'].lower():
        print("Doğru!\n")
        dogru_sayisi += 1
    else:
        print(f"Yanlış! Doğru cevap: {soru['cevap']}\n")

puan = (dogru_sayisi / toplam_soru) * 100
print(f"Quiz tamamlandı! Toplam puanınız: {puan: }")

