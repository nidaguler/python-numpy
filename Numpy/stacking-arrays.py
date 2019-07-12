#stacking arrays yani arrayleri istedigimiz duzende birlestirme islemi
import numpy as np
array1=np.array([[1,2],[3,4]])
array2=np.array([[-1,-2],[-3,-4]])

#vertical - dikey birlestirme

#array([[1,2],
#       [3,4]])
#array=([[-1,-2],
#       [-3,-4]])
#horizontal - yatay birlestirme
#array([[1,2],[-1,-2]],
#      [3,4],[-3,-4])

array3=np.vstack((array1,array2)) #vstack vertical birlestirme metodu
print(array3)
#sonuc
"""
[[ 1  2]
 [ 3  4]
 [-1 -2]
 [-3 -4]]
"""
array4=np.hstack((array1,array2))#horizontal birlestirme
print(array4)
#sonuc
"""
[[ 1  2 -1 -2]
 [ 3  4 -3 -4]]
"""