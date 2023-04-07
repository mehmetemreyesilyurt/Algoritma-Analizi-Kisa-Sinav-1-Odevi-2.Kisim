import math
import operator

#Yakınlıkları hesaplanacak noktaların koordinatları girilir.
x1dizisi=[2,3,3,4,5,6,7,9,11,10]
x2dizisi=[4,6,4,10,8,3,9,7,7,2]
ydizisi=[0,1,1,0,0,1,1,0,0,0]
uzakliklar=[]
kalanlar=[]

#Kullanıcıdan alınacak değerler girilir.
k=input("k değerini giriniz. = ")
x1=input("x1 değerini giriniz. = ")
x2=input("x2 değerini giriniz. = ")

k=int(k)
x1=int(x1)
x2=int(x2)

#Uzaklığı belirleyecek formül tanımlanır.
def oklidformulu(x1,x2,y1,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

#Diziye elemanlar eklenir.
for i in range(0,10):
    uzakliklar.append(oklidformulu(x1,x1dizisi[i],x2,x2dizisi[i]))

#Sözlük tanımlanır.
sozluk=dict(zip(uzakliklar,ydizisi))

#Sözlük sıralanır.
sorted_x = sorted(sozluk.items(), key=operator.itemgetter(0))

#K değerine göre noktalar seçilir.
toplam=0
sayac=0
for i in sorted_x:
    if(sayac<k):
        print("{} {}".format(i[0], i[1]))
        toplam=toplam+i[1]
        sayac=sayac+1

#Değerlerin tekrar sayısına göre sonuç bulunur.
ortalama=toplam/k
if(ortalama<0.5):
    print("Sonuç : Kötü")
else:
    print("Sonuç : İyi")