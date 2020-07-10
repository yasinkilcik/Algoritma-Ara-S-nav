#GitHub'a yükledim Hesabım: yasinkilcik https://github.com/yasinkilcik?tab=repositories

#SORU 1
a = int(input('Gün giriniz'))
while a<1 or a>31:
    print("Gün 1 ve 31 arasında girilmelidir")
    a = int(input('Günü tekrar giriniz'))
s = int(input('Ay giriniz'))
while s<1 or s>12:
    print("Ay 1 ve 12 arasında girilmelidir")
    s = int(input('Ayı tekrar giriniz'))

i = int(input('Yıl giriniz'))

n=dict({1:"Ocak", 2:"Şubat", 3:"Mart", 4:"Nisan", 5:"Mayıs", 6:"Haziran", 7:"Temmuz", 8:"Ağustos", 9:"Eylül", 10:"Ekim", 11:"Kasım", 12:"Aralık"})

print(a,n[s],i)




#SORU 2
y = int(input('16 dan küçük ve negatif olmayan bir sayı giriniz.'))
a=1
while y>=16 or y<0:
    y = int(input('Hatalı sayı girdiniz. Tekrar girin'))

if y<16 and y>=9:
    i = 0
    for a in range(y+1):
        s=2*a
        i=s+i
        a=a+1
    print("girilen sayı 16 ve 9 arasındadır (9 dahil) toplam: ",i)
elif y<9 and y>=0:
    i = 0
    for a in range(y+1):
        n = 3 * a
        i = n + i
        a = a + 1
    print("girilen sayı 9 ve 0 arasındadır (0 dahil) toplam: ",i)





#SORU 3
from scipy import mat

A = mat('[1 2 -1; 2 5 2; -1 -2 2]')
y=dict({"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26})





#SORU 4
print(1, "ile", "07 arasındaki asal sayılar:")
y=list()
for a in range(7):
    if a > 1:
        for s in range(2, a):
            if (a % s) == 0:
                break
        else:
            y.append(a)

print(y)
