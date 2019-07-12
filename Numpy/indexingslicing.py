import numpy as np

array=np.array([1,2,3,4,5,6,7])
print(array[0])#belirlediğimiz indexteki elemani cagirmak
#sonuc 1

print(array[0:4])#Sifirdan 4.indexe kadar olan elemanlari yazdirir. Sifir dahildir, dort dahil değildir.
#sonuc
"""
[1 2 3 4]
"""

reverse_array=array[::-1]#arrayi ters cevirir.
print(reverse_array)
#sonuc
"""
[7 6 5 4 3 2 1]
"""

array1=np.array([[1,2,3,4,5],[6,7,8,9,10]]) #2 boyutlu array
print(array1)
#iki boyutlu oldugunu gosterelim
"""
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
"""
#yukardak matriste 7 değerine erismek icin ornek yapalim
print(array1[1,1])#7 değeri 1. satir 1. sutun bulunuyor
#sonuc
"""
7
"""
print(array1[:,1])#buradaki iki nokta isareti satirlari ifade eder.
#sonuc
"""
[2 7]
"""
#istedigimiz bolumlerden secerek baska bi ornek yapalim
print(array1[1,1:4])#1. indexe sahip satir ve 1. index ike 4. index arasindaki  sutunu alacagımızı yazdık
#sonuc
"""
[7 8 9]
"""

print(array1[-1:])#son satiri alma ornegi
#sonuc
"""
[[ 6  7  8  9 10]]
"""
print(array1[:,-1])#son sutunu alma ornegi
"""
[ 5 10]
"""

