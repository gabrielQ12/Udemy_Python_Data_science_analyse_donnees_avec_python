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
import pandas as pd

food_info = pd.read_csv("food_info.csv")

# Objet series représentant la colonne "NDB_No"


# 1 methode 

ndb_col = food_info["NDB_No"]

# ici on a crée un objet series qui represente la colonne "NDB_N0" de notre dataframe food_info



# 2 methode avec une variable pour le nom de la colonne

col_name = "NDB_No"
ndb_col = food_info[col_name]

print(ndb_col)
```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

protein = food_info["Protein_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]

print(protein)
print(cholesterol)
```
------
```Python

import pandas as pd

food_info = pd.read_csv("food_info.csv")

# methode 1 

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]

# ici on a selectionné les colonnes Zinc_(mg) et Copper_(mg) et 
# on les a stocké dans la variable zinc_copper pour affiché les 2 colonnes 

# methode 2 

zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

# ici on a selectionné les colonnes Zinc_(mg) et Copper_(mg) et 
# on les a stocké dans la variable zinc_copper pour affiché les 2 colonnes 

print(zinc_copper)

```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

selenium_thiamin = food_info [["Shrt_Desc", "Selenium_(mcg)" , "Thiamin_(mg)"]]
print(selenium_thiamin)
```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

col_names = food_info.columns.tolist()
gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
        
# ici la boucle for permet de récupérer les colonnes qui se terminent par (g) 
# grace a la methode endswith() et de les stocker dans une liste
# ensuite on utilise cette liste pour selectionner les colonnes du dataframe
        
gram_df = food_info[gram_columns]

# on affiche les 3 premieres lignes du dataframe avec toutes les colonnes qui se terminent par (g)

print(gram_df.head(3))

```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

# score = 2 x protein - 0.75 x lipide 

col_names = food_info.columns.tolist()

div_1000 = food_info["Iron_(mg)"] / 1000

iron = food_info["Iron_(mg)"]

# Ajoute 100 à chaque veleur dans la colonne et retourne un nouvel objet series

add_100 = food_info["Iron_(mg)"] + 100

# soustrai 100 a chaque valeur de la colonne et retourne un nouvel objet series

sub_100 = food_info["Iron_(mg)"] - 100

# Multiplie chaque valeur de la colonne par 2 et retourne un nouvel objet series

mult_2 = food_info["Iron_(mg)"] * 2



```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

# score = 2 x protein - 0.75 x lipide 

col_names = food_info.columns.tolist()

sodium_grams = food_info["Sodium_(mg)"] / 1000

sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000

print(sodium_grams)
print(sugar_milligrams)

```
------
```Python

import pandas as pd

food_info = pd.read_csv("food_info.csv")

water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy[0:5])

# ici on multiplie les valeurs de la colonne "Water_(g)" par les valeurs de la colonne "Energ_Kcal" pour chaque ligne
# on obtient un objet Series avec les valeurs résultantes


grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]

print(grams_of_protein_per_gram_of_water)
print("**delimiter**")
print(milligrams_of_calcium_and_iron)

```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

protein = food_info["Protein_(g)"] *2
fat = food_info["Lipid_Tot_(g)"] * -0.75

rating = protein + fat

print(rating)

```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

# series.max() permet de trouver la valeur maximale dans une série

max_calories = food_info["Energ_Kcal"].max() 

# ici on trouve la valeur maximale de la colonne "Energ_Kcal" dans le dataframe food_info
# on peut aussi utiliser la méthode .min() pour trouver la valeur minimale
# on peut aussi utiliser la méthode .mean() pour trouver la moyenne
# on peut aussi utiliser la méthode .sum() pour trouver la somme
# on peut aussi utiliser la méthode .std() pour trouver l'écart type
# on peut aussi utiliser la méthode .median() pour trouver la médiane
# on peut aussi utiliser la méthode .mode() pour trouver le mode
# on peut aussi utiliser la méthode .value_counts() pour trouver le nombre de fois que chaque valeur apparaît
# on peut aussi utiliser la méthode .describe() pour obtenir des statistiques sommaires pour chaque colonne
# on peut aussi utiliser la méthode .corr() pour obtenir la corrélation entre les colonnes
# on peut aussi utiliser la méthode .cov() pour obtenir la covariance entre les colonnes
# on peut aussi utiliser la méthode .kurt() pour obtenir l'aplatissement des colonnes
# on peut aussi utiliser la méthode .skew() pour obtenir l'asymétrie des colonnes
# on peut aussi utiliser la méthode .abs() pour obtenir la valeur absolue des colonnes
# on peut aussi utiliser la méthode .round() pour arrondir les valeurs des colonnes
# on peut aussi utiliser la méthode .cumsum() pour obtenir la somme cumulée des colonnes
# on peut aussi utiliser la méthode .cummax() pour obtenir le maximum cumulé des colonnes
# on peut aussi utiliser la méthode .cummin() pour obtenir le minimum cumulé des colonnes
# on peut aussi utiliser la méthode .cumprod() pour obtenir le produit cumulé des colonnes
# on peut aussi utiliser la méthode .diff() pour obtenir la différence entre les colonnes
# on peut aussi utiliser la méthode .pct_change() pour obtenir le pourcentage de changement entre les colonnes
# on peut aussi utiliser la méthode .rank() pour obtenir le rang de chaque valeur dans les colonnes
# on peut aussi utiliser la méthode .sort_values() pour trier les valeurs dans les colonnes
# on peut aussi utiliser la méthode .sort_index() pour trier les index dans les colonnes

# Diviser les valeurs de la colonnes "energy_kcal" par la valeur maximale de cette colonne

normalized_calories = food_info["Energ_Kcal"] / max_calories
print(normalized_calories)

# ici on divise chaque valeur de la colonne "Energ_Kcal" par la valeur maximale de cette colonne
# ce qui nous retourne un objet Series avec les valeurs normalisées

```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")



max_calories = food_info["Energ_Kcal"].max() 



normalized_calories = food_info["Energ_Kcal"] / max_calories
print(normalized_calories)

normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()

print("**delimiter**")
print(normalized_protein)
print("**delimiter**")
print(normalized_fat)

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
