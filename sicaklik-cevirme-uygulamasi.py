print("Sıcaklık çevirme uygulamasına hoşgeldiniz.")
print("1 - Celcius / Kelvin Çevirme")
print("2 - Celcius / Fahrenhayt Çevirme\n")
print("3 - Kelvin / Celcius Çevirme")
print("4 - Kelvin / Fahrenhayt Çevirme\n")
print("5 - Fahrenhayt / Celcius Çeirme")
print("6 - Fahrenhayt / Kelvin Çevirme")

# buraya sıcaklık değerlerimizi giriyoruz.
kelvin2 = -273.15
kelvin = 273.15
fahrenhayt = 32

secim = int(input("Lütfen çeviri yapmak istediğiniz numarayı giriniz: "))
derece = int(input("Lütfen çevirmek istediğiniz dereceyi giriniz: "))

if secim == 1:
    print("Çevirme sonucunuz",kelvin + derece)

elif secim == 2:
    print("Çevirme sonucunuz:",fahrenhayt + derece)

elif secim == 3:
    print("Çevirme sonucunuz:",derece + kelvin2)

elif secim == 4:
    print("Çevirme sonucunuz:",derece * 9 / 5 - 459.67) # burda alından değeri 9 ile çarpıp 5 e bölüyoruz ardından 459.67 çıkarıyoruz. bu hesabı ben yapmadım bir siteden gördüm

elif secim == 5:
    print("Çevirme sonucunuz:",(derece - 32) * 5 / 9) # bu işlemi aynı şekilde ben yapmadım

elif secim == 6:
    print("Çevirme sonucunuz:",(derece + 459.67) * 5 / 9) # bu da aynı şekilde