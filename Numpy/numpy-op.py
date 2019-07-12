# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 03:48:08 2019

@author: ben
"""

import numpy as np #numpy kütüphanesini import et

a= np.array([1,2,3])#a degiskenine bir dizi ata.
b=np.array([4,5,6])#b degiskenine bir dizi ata.
#iki dizinin de boyutlarının aynı olması onemli
"""
dizi indexleri sifirdan baslar.
matematiksel işlemlerde iki dizide de toplama,cikarma gibi islemler yaparken 
birinci dizinin sifirinci indexe sahip elemani ile ikinci dizinin sifirinci indexe sahip elemani,
birinci dizinin birinci indexe sahip elemani ile ikinci dizinin birinci indexe sahip elamani, 
birinci dizinin ikinci indexe sahip elemani ile ikinci dizinin ikinci indexe sahip elemani uzerinde islem yapılır.
oncelik bu sekildedir eger ki sira ya da index belirlemezsek. 
"""
print(a+b)#toplayıp ekrana yazdir
#sonuc
"""
birinci dizinin sifirinci indexe sahip elemani 1 ve ikinci dizinin sifirinci indexe sahip elemani 4 
bu yuzden sonucta gorulen sifirinci indexe sahip satir ve sifirinci indexe sahip kolonda 4+1 yani 5 yaziyor.
birinci dizinin birinci indexe sahip elemani 2 ve ikinci dizinin birinci indexe sahip elemani 5
bu yuzden soncucta gorulen sifirinci indexe sahip satir ve birinci indexe sahip kolonda 2+5 yani 7 yaziyor.
birinci dizinin ikinci indexe sahip elemani 3 ve ikinci dizinin ikinci indexe sahip elemani 6 
bu yuzden sonucta gorulen sifirinci indexe sahip satir ve ikinci indexe sahip kolonda 3+6 yani 9 yaziyor.
ayni islem sirasi diğer islemlerde de gecerli oldugu icin bu mantikta ilerleyin toplama,cikarma,carpma fark etmez.

[5 7 9]
"""
print(a-b)#cikarip ekrana yazdir
#sonuc
"""
[-3 -3 -3]
"""
print(a**2)#iki yildiz isareti karesi anlamina gelir.
#sonuc
"""
[1 4 9]
"""

#sinus alma
print(np.sin(a))#np.sin metodu ile a degiskenine atanmis dizinin sinusunu almis olduk
"""
dizi icindeki bosluk kaydırmalari anlasilsin diye yapildi.
islem oncesi ->  [1,      2,         3]
sinus hali -> [0.84147098 0.90929743 0.14112001]
"""
print(np.sin(b))#np.sin metodu ile b degiskenine atanmis dizinin sinusunu almis olduk
#sonuc
"""
dizi icindeki bosluk kaydirmalari anlasilsin diye yapildi
islem oncesi -> [4,           5,          6]
sinus hali ->   [-0.7568025  -0.95892427 -0.2794155 ]
"""

#conditionals ornegi
a<2
#sonuc
"""
a degiskenine atanmis dizideki elemanlari 2den kucuk
olanlara gore uyarlamasini istedik.
simdi tek tek bakalim.
a degiskenine atanmis dizinin sifirinci indexteki elemani 1
1<2 dogru yani true, 
a degiskenine atanmis dizinin birinci indexe sahip elemani 2
2<2 yanlis yani false,
a degiskenine atanmis dizinin ikinci indexe sahip elemani 3
3<2 yanlis yani false.
array([ True, False, False])
"""

#iki tane ayni dizi olusturalim. Ayni olmalari bi sorun teskil etmez.
a=np.array([[1,2,3],[4,5,6]])#basta ve sonda ikiser koseli parantez olmasi sart
b=np.array([[1,2,3],[4,5,6]])#basta ve sonda ikiser koseli parantez olmasi sart

#element wise product
"""
 yani bunu bire bir islem yapmak gibi dusunebiliriz.
1 ile 1i carp,2 ile 2yi carp vs.
diziler ayni oldugu icin karesini almayla ayni islemi yaptik birbiriyle carparak
"""
print(a*b)#a ile b yi carpip ekrana yazdiralim
#sonuc
"""
[[ 1  4  9]
 [16 25 36]]
"""
#matrix product - matrisler
a.dot(b)#bunu yazdigimizda hata aliriz cunku dizi boyutlarinin 3,2 ve 2,3 gibi olmasi gerekir.
a.dot(b.T)#b.T yazidigimizda bnin transpozunu alip sorunsuz carpim yapmis oluruz.
#transpoz dogrusal cebirde matrisin satir ve sutunlarinin yer degistirmesi demektir.
#sonuc
"""
array([[14, 32],
       [32, 77]])
"""
#exponential yani eksponalsiyel
print(np.exp(a))#a nin eksponansiyelini aldik. ekponansiyel sabit artis veya azalis degisimini belirtir.
"""
[[  2.71828183   7.3890561   20.08553692]
 [ 54.59815003 148.4131591  403.42879349]]

"""
a=np.random.random((5,5))#random metodu sifirla bir arasinda random sayilar olusturmaya yarar. biz burada 5*5lik bir matris yazdik
print(a)#olusturdugumuz matrisi ekrana yazdiralim
#sonuc
"""
[[0.42666638 0.7395227  0.28028156 0.68978795 0.51017682]
 [0.76512234 0.59441761 0.19382303 0.63771471 0.92007518]
 [0.65072753 0.36000526 0.9807365  0.46102458 0.08452672]
 [0.58841358 0.735464   0.06509236 0.43472321 0.83424131]
 [0.67503191 0.61013617 0.32394976 0.38644048 0.75947792]]
"""
print(a.sum())#yukarıda olusturdugumuz 5*5lik matristeki sayilari toplayalim.
#sonuc
"""
13.707579594417618
"""
print(a.max())#yukarıda olusturdugumuz 5*5lik matriste random sayilar arasindaki maksimum degeri bulma
#sonuc
"""
0.9807364991366305
"""
print(a.min())# yukarıda olusturdugumuz 5*5lik matriste random sayilar arasindaki minimum degeri bulma
#sonuc
"""
0.06509235752712705
"""
print(a.sum(axis=0))#yukarıda olusturdugumuz 5*5lik matristeki kolonları axis=0 yazarak topluyoruz.
#sonuc
"""
aciklayici olması icin matrisi komple ekleyip toplama ok yonlerini koydum 
[[0.42666638 0.7395227  0.28028156 0.68978795 0.51017682]
 [0.76512234 0.59441761 0.19382303 0.63771471 0.92007518]
 [0.65072753 0.36000526 0.9807365  0.46102458 0.08452672]
 [0.58841358 0.735464   0.06509236 0.43472321 0.83424131]
 [0.67503191 0.61013617 0.32394976 0.38644048 0.75947792]]
       |        |           |         |         | 
       ^        ^           ^         ^         ^  
[3.10596174 3.03954575 1.8438832  2.60969093 3.10849796] <-sonuc
"""
print(a.sum(axis=1))##yukarıda olusturdugumuz 5*5lik matristeki satirlari axis=1 yazarak topluyoruz.
#sonuc
"""
aciklayici olması icin matrisi komple ekleyip toplamanin ok yonlerini koydum 
[[0.42666638 0.7395227  0.28028156 0.68978795 0.51017682] -> 2.64643542
 [0.76512234 0.59441761 0.19382303 0.63771471 0.92007518] -> 3.11115287
 [0.65072753 0.36000526 0.9807365  0.46102458 0.08452672] -> 2.53702059
 [0.58841358 0.735464   0.06509236 0.43472321 0.83424131] -> 2.65793446
 [0.67503191 0.61013617 0.32394976 0.38644048 0.75947792]] -> 2.75503625
      
#[2.64643542 3.11115287 2.53702059 2.65793446 2.75503625] <- sonuc
"""

print(np.sqrt(a))#yukarida olusturdugumuz 5*5lik matrisin kokunu alalim
#sonuc
"""
[[0.65319705 0.85995506 0.52941624 0.83053474 0.71426663]
 [0.87471272 0.77098483 0.44025337 0.79857042 0.9592055 ]
 [0.80667685 0.60000439 0.99032141 0.67898791 0.29073479]
 [0.76708121 0.85759198 0.25513204 0.65933543 0.91336812]
 [0.82160326 0.78111214 0.56916584 0.62164337 0.87148031]]
"""
print(np.square(a))#yukarida olusturdugumuz 5*5lik matrisin karesini alalim
#sonuc
"""
[[0.1820442  0.54689382 0.07855775 0.47580742 0.26028039]
 [0.58541219 0.3533323  0.03756737 0.40668005 0.84653834]
 [0.42344632 0.12960379 0.96184408 0.21254366 0.00714477]
 [0.34623054 0.5409073  0.00423702 0.18898427 0.69595857]
 [0.45566808 0.37226615 0.10494345 0.14933625 0.57680671]]
"""
print(np.add(a,a))#yukarida olusturdugumuz 5*5lik matrisin birbiriyle toplanmasi yani a+a yazmak yerine baska bir yol add metoduna 2 kere ayni matrisi yazmis oluyoruz a,a diyerek
#sonuc
"""
[[0.85333276 1.4790454  0.56056312 1.3795759  1.02035365]
 [1.53024468 1.18883523 0.38764606 1.27542942 1.84015036]
 [1.30145507 0.72001053 1.961473   0.92204915 0.16905344]
 [1.17682716 1.470928   0.13018472 0.86944642 1.66848263]
 [1.35006382 1.22027234 0.64789952 0.77288096 1.51895584]]
"""













