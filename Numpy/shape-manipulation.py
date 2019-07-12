import numpy as np

array=np.array([[1,2,3],[4,5,6],[7,8,9]])#3*3luk bir array olusturduk
print(array)
#calistiralim
"""
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
"""
a = array.ravel()#arrayi tek satirlik bir vektor haline donusturur.
print(a)
#sonuc
"""
[1 2 3 4 5 6 7 8 9]
"""
array2=array.reshape(3,3)#yukarida tek satirlik vektorumuzu 3*3luk bir matrise donusturecegiz
print(array2)
#sonuc
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
#yukaridaki matrisin transpozunu alacagız
arrayT=array2.T #transpoz alma islemi
print(arrayT)
#sonuc
"""
[[1 4 7]
 [2 5 8]
 [3 6 9]]
"""
#kaca kaclik bir matrisimiz oldugunu ogrenelim
print(arrayT.shape)
#sonuc
"""
(3, 3)
"""
#3*2lik bir matris olusturalim
array5=np.array([[1,2],[3,4],[5,6]])
print(array5)
#sonuc
"""
[[1 2]
 [3 4]
 [5 6]]
"""
#simdi bu matrisi 2*3luk bir matrise donusturelim
print(array5.reshape(2,3))
#sonuc
"""
[[1 2 3]
 [4 5 6]]

"""
"""
reshape ile resize arasındaki fark;
reshape ettigimiz matrisi baska bir degiskene atamamiz gerekiyor.
resize ettigimizde bunu kaydetmedigi icin matrisimizde bi degisiklik olmuyor.

"""



