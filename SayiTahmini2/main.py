import random
import math
import time

baslangic = time.time()
min, max, sayac = 0, 10000, 0
sayi = random.randint(min, max)

print(f"Rastgele sayı: {sayi}")

while True:
    number = math.floor((min + max) / 2)

    if number < sayi:
        print(f"{number} değerinden daha büyük bir sayı tahmin ediniz ({min}, {max} arasında)")
        min = number
        sayac += 1
    elif number > sayi:
        print(f"{number} değerinden daha küçük bir sayı tahmin ediniz ({min}, {max} arasında)")
        max = number
        sayac += 1
    else:
        print(f"İkiye bölme yöntemi ile {number} tahmininizi {sayac} denemede doğru bildiniz")
        break

bitis = time.time()
sonuc=bitis-baslangic
print("Bu işlemde  geçen süre {}".format(sonuc))