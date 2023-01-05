# Palindrom, tersten okunuşu da aynı olan cümle, sözcük ve sayılara denilmektedir.

#a = "1234554321"
a = input('Kontrol etmek istediğiniz kelime ya da sayıyı giriniz: ')
a = str(a)
def is_palindrome(str):
    return str == a[::-1]

if is_palindrome(a):
    print("Evet, '{}' bir palindrom".format(a))
else:
    print("Hayır, '{}' bir palindrom değil".format(a))


