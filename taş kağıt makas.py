import random
import time

while True:
    options = ["taş", "kağıt", "makas"]
    computer_preference = random.choice(options)
    human_choice = input("Lütfen taş, kağıt veya makas tercihinizi girin: ")

    time.sleep(1)
    
    if computer_preference == "taş" and human_choice == "kağıt":
        print("Kazanan: Siz")
    elif computer_preference == "taş" and human_choice == "makas":
        print("Kazanan: Bilgisayar")
    elif computer_preference == "kağıt" and human_choice == "taş":
        print("Kazanan: Bilgisayar")
    elif computer_preference == "kağıt" and human_choice == "makas":
        print("Kazanan: Siz")
    elif computer_preference == "makas" and human_choice == "taş":
        print("Kazanan: Siz")
    elif computer_preference == "makas" and human_choice == "kağıt":
        print("Kazanan: Bilgisayar")
    elif computer_preference == human_choice:
        print("Berabere!")
    else:
        print("Lütfen geçerli bir tercih yapın (taş, kağıt veya makas).")

    print(f"senin tercihin: {human_choice}")
    print(f"bilgisayarın tercihi: {computer_preference}")