import random
import time

x=random.randint(1,32)
print(x)

converted_to_lira = lambda dolar: dolar * x

def main():
    print("Doları Türk parasına çeviriciye hoş geldiniz!           ")
    print()
    time.sleep(5)

    dolar = float(input("Lütfen dolar miktarını giriniz: "))
    lira = converted_to_lira(dolar)

    print(f"{dolar} dolar, {lira:.2f} Türk lirasına eşdeğerdir.")

main()
