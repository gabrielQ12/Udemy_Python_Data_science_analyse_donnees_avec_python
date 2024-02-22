```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

# ici nous avons créer un objet de type DataFrame



# head() permet d'afficher les 5 premières lignes du DataFrame
# si on veut afficher les 10 premières lignes on peut faire food_info.head(10)



column_names = food_info.columns

# ici on affiche les noms des colonnes

# dimensions du DataFrame

dimensions = food_info.shape

# ici on affiche les dimensions du DataFrame

num_rows = dimensions[0]

# ici on affiche le nombre de lignes du DataFrame

num_cols = dimensions[1]

# ici on affiche le nombre de colonnes du DataFrame
```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

# Objet series représentanr la ligne d'index 0 ou de la première ligne

print(food_info.loc[0])

# ici on a un objet series qui représente la première ligne du dataframe food_info

print(type(food_info.loc[0]))
```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

row_100 = food_info.loc[99]

# ici on a affiché la 100ème ligne du dataframe food_info

print(row_100)

```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

row_100 = food_info.loc[99]

print(row_100)

# le type Objet représente une chaine de caractères
# le type Int64 représente un entier
# le type Float64 représente un décimal
# le type datetime64 représente une date
# le type bool représente une valeur booléenne

print(food_info.dtypes)

#ici on affiche le type de chaque colonne

```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

# Dataframe contenant les lignes d'index 3, 4, 5 et 6 

food_info.loc[3:6]

# ici on a utilisé la méthode loc[] pour sélectionner les lignes 3 à 6 de food_info.

# print(food_info.loc[3:6])

# Dataframe contenant les lignes d'index 2, 5 et 10.

# méthode 1
two_five_ten = [2,5,10]
food_info.loc[two_five_ten]
# print(food_info.loc[two_five_ten])

#méthode 2 

food_info.loc[[2,5,10]]
# print(food_info.loc[[2,5,10]])

num_rows = food_info.shape[0]
last_rows = food_info.loc[num_rows-5:num_rows-1]

# ici on a utilisé la méthode shape et la méthode loc[] pour sélectionner les 5 dernières lignes de food_info.

print(last_rows)

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
------
```Python

```
------
