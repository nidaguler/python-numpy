#convert and copy array yani arrayden listeye, listeden arraye donusum yapma
import numpy as np
#listeden numpy arraye donusturme
liste=[1,2,3,4] #normal liste
#array=np.array([1,2,3,4]) numpy ile olusturdugumuz dizi
array=np.array(liste)#donusturme islemi
print(array)
type(array)#sonuc numpy.ndarray
#sonuc
"""
[1 2 3 4]
"""
#arrayden listeye donusturme
liste2=list(array)
print(liste2)
type(liste2)# sonuc list
#sonuc
"""
[1 2 3 4]
"""
#copy
a=np.array([1,2,3,4])
b=a
c=a
print(a) #sonuc [1 2 3 4]
print(b) #sonuc [1 2 3 4]
print(c) #sonuc [1 2 3 4]
#22. satirdan 27. satira kadar secip run ettigimizde yukarıdaki sonuclari elde ederiz. c yi degistirip bakalim
c[0]=7
#simdi 22. satirdan 33.satira kadar secip run edelim. bakin hepsi degisti
print(a) #sonuc [7 2 3 4]
print(b) #sonuc [7 2 3 4]
print(c) #sonuc [7 2 3 4]

"""
burada c[0]=7 islemini yaptigimizda a da, b de, c de degisir.
bunun sebebi memoryde hepsinin aynı alanda olması. 
bunun cozumu ise copy yazarak farklı bi alan ayırmak
"""
d=np.array([1,2,3])
print(d) #sonuc [1 2 3 ]
e=d.copy() 
print(e) #sonuc [1 2 3 ]
f=d.copy()
print(f) #sonuc [1 2 3 ]
#40. satirdan 45e kadar secip calistirdigimizda yukaridaki sonuclari elde ederiz
#simdi f yi degistirelim ve 40. satirdan 51. satira kadar secip run edelim.
f[0]=9#normalde fnin sifirinci indexindeki eleman 1 ama simdi 9 olacak ve yalniz f degisecek
print(d) #sonuc [1 2 3]
print(e) #sonuc [1 2 3]
print(f) #sonuc [9 2 3] goruldugu gibi sifirinci indexteki eleman 9 oldu
