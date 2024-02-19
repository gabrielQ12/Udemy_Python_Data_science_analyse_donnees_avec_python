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
import numpy as np

wordl_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1)

## ici U75 est le type de données que nous voulons pour notre tableau numpy cela correspond à 
## des chaines de caractères de 75 caractères maximum

## ici skip_header=1 permet de sauter la première ligne du fichier csv

print(wordl_alcohol) 

```
------
```Python
import numpy as np

matrix = np.array([[5, 10, 15], [20, 25, 30]])

output_value = matrix[1,2]

## ici la première valeur est la ligne et la deuxième valeur est la colonne
## 1 represente la second liste de l'index et 2 represente la troisième valeur de l'index 
## donc la troisième valeur de la second liste ==> ici on a donc la valeur 30

print(output_value) 

```
------
```Python
import numpy as np

wordl_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1)

ivoire_1985 = wordl_alcohol[2,4]
print(ivoire_1985)

second_country = wordl_alcohol[1,2]
print(second_country)
```
------
```Python
import numpy as np

vector = np.array([5, 10, 15, 20])

output_value  = vector[0:3]


print(output_value )


matrix = np.array([[5, 10, 15], 
                   [20, 25, 30], 
                   [35, 40, 45]])

output_value2 = matrix[:,1]

## ici on a pris toutes les lignes de la second colonne (index 1)

print(output_value2)

output_value3 = matrix[2,:]

## ici on a pris toutes les colonnes de la 3eme ligne (index 2)

print(output_value3)

output_value4 = matrix[1:3,1]

## ici on a pris la 2eme et 3eme ligne de la 2eme colonne

print(output_value4)    
```
------
```Python
import numpy as np


world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1)

countries = world_alcohol[:,2]

print(countries)

alcohol_consumption = world_alcohol[ :,4]

print(alcohol_consumption)
```
------
```Python
import numpy as np

matrix = np.array([[5, 10, 15], 
                   [20, 25, 30], 
                   [35, 40, 45]])

output_value = matrix[:,0:2]

## ici on a pris toutes les lignes et les colonnes de 0 à 2 exclu (on affiche donc les index 10 et 1 c'est a dire les colonnes 1 et 2)

print(output_value)

output_value2 = matrix[1:3,:]

## ici on a pris les lignes de 1 à 3 exclu et toutes les colonnes

print(output_value2)

output_value3 = matrix[1:3,0:2]

## ici on a pris les lignes de 1 à 3 exclu et les colonnes de 0 à 2 exclu

print(output_value3)
```
------
```Python
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1)


first_two_columns = world_alcohol[:,0:2]

## ici on a pris toutes les lignes et les deux premières colonnes

print(first_two_columns)

first_ten_years = world_alcohol[0:10,0]

## ici on a pris les dix premières lignes et la première colonne

print(first_ten_years)

first_ten_rows = world_alcohol[0:10,:]

## ici on a pris les dix premières lignes et toutes les colonnes

print(first_ten_rows)

first_twenty_regions = world_alcohol[0:20,1:3]

## ici on a pris les vingt premières lignes et les colonnes 2 et 3

print(first_twenty_regions)
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
