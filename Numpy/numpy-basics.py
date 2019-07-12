# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 03:47:20 2019

@author: ben
"""

import numpy as np #numpy kütüphanesini import et ve kısayol olarak da np ile kullan.

array =np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) #np.array ile numpy kütüphanesinin array metodunu çağırarak dizi oluşturuyoruz.
#yukarıdaki array 1 tane satır 15 tane sütundan oluşan bir vektör

#şimdi dizinin kaça kaçlık bi matris oldugunu ekrana bastıralım
print(array.shape)
#sonuc (15,) geldi. 
#simdi diziyi matrise dönüstürelim bunu reshape ile yapıyoruz.
a=array.reshape(3,5)
#diziyi bi degiskene aktarıp matrise dönüstürelim
#burada 3 satır 5 sütundan olusan bi matris yapmak istedigimizi soyluyoruz.
#sonuc
"""
array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15]])

"""
#ndim ile yani dimension ile kaç boyutlu bir matris oldugunu öğreniyoruz
print(a.ndim) #sonuc: 2
#şimdi arrayin içindeki data tipini bulalım. bunu dtype ile yapıyoruz.
print(a.dtype.name) #sonuc int32
print(a.size) #bunu size ile yapıyoruz. bu bize reshape öncesi boyutu verir. sonuc:15

#reshape yapmadan 2 ya da 3 boyutlu yapmak. bunu [],[],[] seklinde yazarak yapabiliyoruz.örnekleyelim

array1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])#içerde 2şer tane köşeli parantez olmak zorunda
print(array1.shape)#sonuc (3,4) bir matris oldugu

#np.zeros bize sıfırlardan oluşan bir matris verir.
#programlamada buna allocation yani yer ayırtma denir.

np.zeros((3,4))#çift paramtezi unutmayalım.
#sonuc
"""
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
"""
#bunu kullanmamızın sebebi append metodunun hafızayı yorması. append metonun yerine np.zeros ile yer ayırırız.
#daha sonra güncellemek istedigimiz yerde güncelleme yapmamıza olanak sağlar.
#güncelleme denemesi yapalım
zeros=np.zeros((3,4))
zeros[0,0]=5#0. satır ve 0. sütun elemanını 5 olarak güncellemek istedigimizi soyluyoruz.
print(zeros)#güncellenmis halini ekrana bastıralım
#sonuc
"""
array([[5., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
"""
#np.ones ile sıfır yerine birlerden olusan bir matris olustururuz.
np.ones((3,4))#çift parantezi unutmuyoruz.
#sonuc
"""
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
"""

#np.empty ile boş bir matris olustururuz.
np.empty((3,3))#çift parantezi unutmayalım.
#sonuc
"""
mesela burada görülen sayılardan 9.70344928e-321 sayısı 0dan sonra 10 üzeri eksi 321 ile çarpılmış bir sayı
yani oldukça küçük. yukarıda bir sürü metot yazdıgım icin  sayılar tam olarak istediğimiz gibi çıkmadı.
tek başına kullanıldıgında sağlıklı sonuç elde edilir.
yani aslında o alan boş. gidip kendi kafamıza göre sadece bosluk bırakmayız, bu islemi yaparız.
array([[0.00000000e+000, 0.00000000e+000, 0.00000000e+000],
       [0.00000000e+000, 0.00000000e+000, 9.70344928e-321],
       [1.90692349e+189, 7.02189487e+174, 7.76386873e+174]])
"""

a=np.arange(10,50,5)# 10 ile 50 arasındaki sayıları 5er 5er yazdırma
print(a)#ekrana bastıralım
#sonuc
"""
ilk yazdıgımız 10 değeri dahil edilirken 50 degeri dahil edilmedi.
yani inclusive 10, exclusive 50. bunu unutmayalım.bu boyle calisiyor."10dan 50ye" kadar yazar.5 ise arttırma miktarımız.
[10 15 20 25 30 35 40 45]
"""

a=np.linspace(0,10,20)#burada ise 0 "ile" 10 arasında 20 sayı yazdırmak istedigimizi söylüyoruz.
print(a)#ekrana basıralım.
#sonuc
"""
görüldüğü gibi 0 ve 10 dahil bu sefer. kelimeler arasındaki ayrımaları sakın karıstırmayalım.

[ 0.          0.52631579  1.05263158  1.57894737  2.10526316  2.63157895
  3.15789474  3.68421053  4.21052632  4.73684211  5.26315789  5.78947368
  6.31578947  6.84210526  7.36842105  7.89473684  8.42105263  8.94736842
  9.47368421 10.        ]
"""









