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

food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat

print(food_info.head())

```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

# sort_values() est une méthode qui permet de trier un DataFrame par rapport à une colonne

food_info.sort_values("Sodium_(mg)")

# Trier et remplacer l'ancien dataframe

food_info.sort_values("Sodium_(mg)", inplace=True)

# ici inplace=True permet de remplacer l'ancien dataframe par le nouveau dataframe trié

# Trier par ordre décroissant

food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False) 

# ici ascending=False permet de trier par ordre décroissant



```
------
```Python
import pandas as pd

food_info = pd.read_csv("food_info.csv")

pd.isnull()
## ici isnull() est une fonction qui permet de vérifier si une valeur est NaN ou pas
```
------
```Python
# series.mean() est une méthode qui calcule la moyenne de toutes les valeurs dans une série en ignorant les valeur manquante
```
------
```Python
import pandas as pd

titanic_survival= pd.read_csv("titanic_survivalcsv")

fare_by_class = {}
passenger_classes = [1, 2, 3]

for this_class in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class]
    pclass_fares = pclass_rows["Fare"]
    fare_by_class[this_class] = pclass_fares.mean()
    
print(fare_by_class)
```
------
```Python
import pandas as pd
import numpy

titanic_survival= pd.read_csv("titanic_survivalcsv")

# pivot_table() permet de créer des tableaux croisés dynamiques et donc de réorganiser les données pour faire apparaître des informations différentes.

passenger_class_fares=titanic_survival.pivot_table(index="Pclass", values="Fare", aggfunc=numpy.mean)
```
------
```Python
import pandas as pd
import numpy

titanic_survival= pd.read_csv("titanic_survivalcsv")

# .dropna() est une methode qui permet de supprimer les valeurs manquantes
# on utilise (axis=0) pour supprimer les lignes et (axis=1) pour supprimer les colonnes


drop_na_rows = titanic_survival.dropna(axis=0)
print(drop_na_rows)

drop_na_columns = titanic_survival.dropna(axis=1)
print(drop_na_columns)
```
------
```Python
import pandas as pd
import numpy

titanic_survival= pd.read_csv("titanic_survivalcsv")

# .loc() permet de selectionner des lignes et des colonnes par leur label
```
------
```Python
import pandas as pd
import numpy

titanic_survival= pd.read_csv("titanic_survivalcsv")

# reset_index(drop=true) permet de réindexer le dataframe
```
------
```Python
import pandas as pd
import numpy

titanic_survival= pd.read_csv("titanic_survivalcsv")

# .apply() est une method qui permet d'appliquer une fonction sur chaque élément d'une colonne
# si on ajoute (axis=1) a la methode .apply() on applique la fonction a chaque ligne


def row_100(column):
    item = column.loc[99]
    return item

row_100_var = titanic_survival.apply(row_100)
print(row_100_var)
```
------
```Python
# Un objet series peut contenir plusieurs type d'objet :
# float | int | bool | datetime64[ns] | datetime64[ns,tz] | timedelta | category | objet
```
------
```Python
import pandas as pd


# pandas.to_datetime() est une fonction qui convertit les dates en datetime64.

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

# ici, nous avons converti la colonne 'DATE' en datetime64. Nous pouvons maintenant accéder aux attributs de la date
# et utiliser des méthodes pour les manipuler.

```
------
```Python
import pandas as pd

import matplotlib.pyplot as plt


unrate = pd.read_csv('unrate.csv') 

## pyplot est une collection de fonctions dans le module matplotlib 
# il sert a tracer des graphiques et les personnaliser

# plt.plot() sert a tracer un graphique
# plt.show() sert a afficher le graphique

# plt.plot(x_value, y_value) permet de tracer un graphique avec les valeurs de x et y

first_year = unrate[0:12]
plt.plot(first_year['DATE'], first_year['UNRATE'])
plt.show()
```
------
```Python
import pandas as pd

import matplotlib.pyplot as plt


unrate = pd.read_csv('unrate.csv') 


first_year = unrate[0:12]
plt.plot(first_year['DATE'], first_year['UNRATE'])
# plt.xticks(rotation=90) permet de faire pivoter les valeurs de l'axe x de 90°
# matplotlib.pyplot.xticks(*args, **kwargs)
# marche aussi avec yticks
# plt.xticks(rotatio,=45) permet de faire pivoter les valeurs de l'axe x de 45°

plt.plot(first_year['DATE'], first_year['UNRATE'])
plt.xticks(rotation=90)
plt.show()
```
------

```Python
import pandas as pd

import matplotlib.pyplot as plt


unrate = pd.read_csv('unrate.csv') 


first_year = unrate[0:12]

# il est important de bien documenter ses graphiques et les nommer
# plt.xlabel() et plt.ylabel() permettent de nommer les axes x ou y
# plt.title() permet de donner un titre au graphique


plt.plot(first_year['DATE'], first_year['UNRATE'])
plt.xticks(rotation=90)
plt.xlabel('Mois')
plt.ylabel('Taux de chômage (en %)')
plt.title('Evolution du taux de chômage en 1948 au USA')
plt.show()
```
------

```Python
import pandas as pd

import matplotlib.pyplot as plt


unrate = pd.read_csv('unrate.csv') 



fig=plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)


# ici add_subplot(2,1,1) signifie que nous allons ajouter un graphique à la première ligne de la figure,


# axes_object = fig.add_subplot(nrows,ncols, plot_number)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)


# les graphiques ce lisent toujours de gauche à droite et de haut en bas donc 1 en haut à gauche, 2 en haut à droite, 3 en bas à gauche et 4 en bas à droite

fig = plt.figure()
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)


# les graphiques ce lisent toujours de gauche à droite et de haut en bas donc ici on les lis de haut en bas 

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)

ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

plt.show()

# les graphiques ce lisent toujours de gauche à droite et de haut en bas donc ici on les lis de haut en bas mais on a sauté le 2
```
------

```Python
import pandas as pd

import matplotlib.pyplot as plt


unrate = pd.read_csv('unrate.csv') 

x_values = [0.0, 0.5 ,1.0]
y_values = [10, 20, 40]

# ax1.plot(x_values, y_values)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)

ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.plot(x_values, y_values)

plt.show()
```
------

```Python
import pandas as pd

import matplotlib.pyplot as plt


unrate = pd.read_csv('unrate.csv') 

fig = plt.figure(figsize=(15, 8))

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['UNRATE'])
ax1.set_title('Taux de chomage en 1948')


ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['UNRATE'])
ax2.set_title('Taux de chomage en 1949')


plt.show()

# on peu utilisé figsize pour changer la taille de la figure et donc les dimension d'affichage des graphiques

```
------

```Python
import pandas as pd

import matplotlib.pyplot as plt


unrate = pd.read_csv('unrate.csv') 

fig = plt.figure(figsize=(12,12))

for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['UNRATE'])
    
# ici on a 5 graphiques, chacun representant une annee differente ils permettent de voir l'evolution du taux de chomage
    
plt.show()
```
------

```Python
import pandas as pd

import matplotlib.pyplot as plt


unrate = pd.read_csv('unrate.csv') 

# series.dt.month permet de recuperer le mois de la date

# unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(6,6))

plt.plot(unrate[0:12]['MONTH'] , unrate[0:12]['UNRATE'])
plt.plot(unrate[12:24]['MONTH'] , unrate[12:24]['UNRATE'], c='red')

plt.show()
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

