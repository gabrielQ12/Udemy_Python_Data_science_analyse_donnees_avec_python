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
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1) 

print(world_alcohol)

vector = np.array([5, 10, 15, 20])
vector == 10

print(vector == 10)


matrix = np.array([[5,10,15],
                  [20,25,30],
                  [35,40,45]])

matrix == 25

print(matrix == 25)
```
------
```Python
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1) 


vector = np.array([5, 10, 15, 20])

equal_to_ten = (vector == 10)
print(vector[equal_to_ten])


matrix = np.array([[5,10,15],
                  [20,25,30],
                  [35,40,45]])

second_column_25 = (matrix[:,1] == 25)
print(matrix[second_column_25,:])

country_is_algeria = world_alcohol[:,2] == "Algeria"
country_is_algeria = world_alcohol[country_is_algeria]
print(country_is_algeria)

years_is_1984 = world_alcohol[:,0] == "1984"
years_is_1984 = world_alcohol[years_is_1984]
print(years_is_1984)

years_1984 = world_alcohol[world_alcohol[:,0] == "1984"]
print(years_1984)

```
------
```Python
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1) 


vector = np.array([5, 10, 15, 20])

equal_to_ten_and_five = (vector == 10) & ( vector == 5)

# ici on a un tableau de booleen qui nous dit si les elements sont égaux à 10 et 5 
print(equal_to_ten_and_five)

# comme on ne peu pas etre egale a 5 et a 10 a la foi la valeur de retour sera false

equal_to_ten_or_five = (vector == 10) | (vector == 5)

# ici on a un tableau de booleen qui nous dit si les elements sont égaux à 10 ou 5 

print(equal_to_ten_or_five)

is_algeria_and_1986 = (world_alcohol[:,2] == "Algeria") & (world_alcohol[:,0] == "1986")

# ici on a un tableau de booleen qui nous dit si les elements sont égaux à 1986 et algeria

rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

# ici on recupere les lignes qui ont les elements qui sont égaux à 1986 et algeria

print(rows_with_algeria_and_1986)


```
------
```Python

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1) 


vector = np.array([5, 10, 15, 20])

equal_to_ten_or_five = (vector == 10) | (vector == 5)
print(equal_to_ten_or_five)

vector[equal_to_ten_or_five] = 50
print(vector)


matrix = np.array([[5,10,15],
                  [20,25,30],
                  [35,40,45]])

second_column_25 = matrix[:,1] == 25 
print(second_column_25)

matrix[second_column_25, 1] = 10
print(matrix)
```
------
```Python
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1) 


world_alcohol_2 = world_alcohol

world_alcohol_2[:,0][world_alcohol_2[:,0] == '1986'] = '2018'

world_alcohol_2[:,3][world_alcohol_2[:,3] == 'Wine'] = 'Beer'

print(world_alcohol_2)
```
------
```Python
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1) 

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty, 4] = '0'

# astype() est une méthode qui permet de convertir le type d'un tableau numpy

vector = np.array(["1", "2", "3"])
vector = vector.astype(float)

print(vector)

# trouver quel pays bois le plus d'alcool



alcohol_consumption = world_alcohol[:,4]

# ici alcohol_consumption est un tableau de chaine de caractère
# on doit donc le convertir en float pour pouvoir faire des opérations dessus
# on utilise la méthode astype() pour convertir le type de chaque élément du tableau

alcohol_consumption = alcohol_consumption.astype(float)

print(alcohol_consumption)
```
------
```Python
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1) 

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty, 4] = '0'

# astype() est une méthode qui permet de convertir le type d'un tableau numpy

vector = np.array(["1", "2", "3"])
vector = vector.astype(float)


alcohol_consumption = world_alcohol[:,4]

# ici alcohol_consumption est un tableau de chaine de caractère
# on doit donc le convertir en float pour pouvoir faire des opérations dessus
# on utilise la méthode astype() pour convertir le type de chaque élément du tableau

alcohol_consumption = alcohol_consumption.astype(float)

print(alcohol_consumption)
```
------
```Python
import numpy as np

# sum() permet de faire la somme des éléments d'un tableau numpy
# mean() permet de faire la moyenne des éléments d'un tableau numpy
# max() permet de trouver la valeur maximale d'un tableau numpy

vector = np.array([5, 10, 15, 20])

print(vector.sum())

print("**")

print(vector.mean())

print("**")

print(vector.max())

matrix = np.array([[5,10,15],
                  [20,25,30],
                  [35,40,45]])
# dans une matrice on dois spécifier l'axe sur lequel on veux faire l'operation
# axis=0 permet de faire l'operation sur les colonnes
# axis=1 permet de faire l'operation sur les lignes
print("**")
print(matrix.sum(axis=1))
print("**")
print(matrix.sum(axis=0))
```
------
```Python

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1) 


# sum() permet de faire la somme des éléments d'un tableau numpy
# mean() permet de faire la moyenne des éléments d'un tableau numpy
# max() permet de trouver la valeur maximale d'un tableau numpy


# dans une matrice on dois spécifier l'axe sur lequel on veux faire l'operation
# axis=0 permet de faire l'operation sur les colonnes
# axis=1 permet de faire l'operation sur les lignes


is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty, 4] = '0'

# astype() est une méthode qui permet de convertir le type d'un tableau numpy

vector = np.array(["1", "2", "3"])
vector = vector.astype(float)


alcohol_consumption = world_alcohol[:,4]

# ici alcohol_consumption est un tableau de chaine de caractère
# on doit donc le convertir en float pour pouvoir faire des opérations dessus
# on utilise la méthode astype() pour convertir le type de chaque élément du tableau

alcohol_consumption = alcohol_consumption.astype(float)



total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

print(total_alcohol)
print("**")
print(average_alcohol)
```
------
```Python
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1) 

# print(world_alcohol[world_alcohol[:,2] == "Canada"])

is_canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == "1986")
canada_1986 = world_alcohol[is_canada_1986, :]

print(canada_1986)


canada_alcohol = canada_1986[:,4]

print(canada_alcohol)

empty_strings = canada_alcohol == ''
canada_alcohol[empty_strings] = '0'

canada_alcohol = canada_alcohol.astype(float)

print(canada_alcohol)

total_canadian_drinking = canada_alcohol.sum()
print(total_canadian_drinking)

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
------
```Python
```
