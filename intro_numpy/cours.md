```python
import numpy as np

vector = np.array([3, 4, 17, 65])

print(vector)

matrix = np.array([[2, 5, 15], [20, 50, 30], [34, 99, 45]])

print(matrix)
```
------
```Python
import numpy as np


vector = np.array(['1996', 'Western Pacific', 'Viet Nam', 'Wine', '0'])

print(vector)

matrix = np.array([['1996', 'Western Pacific', 'Viet Nam', 'Wine', '0'],
                   ['1986', 'Americas', 'Uruguay', 'Other', '0.5'],
                   ['1985', 'Africa', 'Côte d\'Ivoire', 'Wine', '1.62']])
print(matrix)
```
------
```Python
import numpy as np


vector = np.array([1, 2, 3, 4])
print(vector.shape)

## ici shape est un attribut de l'objet vector qui retourne le nombre d'éléments dans le tableau

matrix = np.array([[5, 10, 15],
                   [20, 25, 30]])
print(matrix.shape)

## ici shape est un attribut de l'objet matrix qui retourne le nombre de lignes et de colonnes dans le tableau
```
------
```Python
import numpy as np

# Fonction numpy pour lire un dataset : numpy.genfromtxt()

wordl_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',')

## ici on lit le fichier world_alcohol.csv et on le stocke dans la variable wordl_alcohol
## delimiter=',' : on spécifie que le fichier est séparé par des virgules


print(type(wordl_alcohol))
print(wordl_alcohol.shape)

wordl_alcohol_dtype = wordl_alcohol.dtype
print(wordl_alcohol_dtype)
```
------
```Python
```
------
```Python
```
------
```Python
```
------
```Python
```
------
```Python
```
------
```Python
```
