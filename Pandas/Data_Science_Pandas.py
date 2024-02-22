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