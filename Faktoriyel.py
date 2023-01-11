c = 1
while c == 1:
    a = int(input('Sayıyı giriniz: '))
    sonuc = 1
    if a > 0:
        for i in range(1, a+1):
            sonuc = sonuc * i
        print("{} sayısının faktoriyeli {} dır.\n(Çıkmak için 0'ı tuşlayınız)".format(a, sonuc))
    elif a == 0:
        print('çıkılıyor..')
        c = 0
    else:
        print ("Negatif sayıların faktöriyeli olmaz!")

