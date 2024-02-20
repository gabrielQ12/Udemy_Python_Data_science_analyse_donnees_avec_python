import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',', dtype="U75", skip_header=1)

totals = {}
is_year = world_alcohol[:, 0] == "1989"
year = world_alcohol[is_year, :]
countries = world_alcohol[:, 2]

for country in countries:
    is_country = year[:, 2] == country
    country_consumption = year[is_country, :]
    alcohol_column = country_consumption[:, 4]
    is_empty = alcohol_column == ''
    alcohol_column[is_empty] = '0'
    alcohol_column = alcohol_column.astype(float)
    totals[country] = np.sum(alcohol_column)
    
# ici la boucle for est utilisée pour parcourir les éléments de la liste countries
# pour chaque élément de la liste, on vérifie si la valeur de la colonne 2 de l'array year est égale à l'élément de la liste
# si c'est le cas, on extrait les lignes correspondantes et on calcule la somme des valeurs de la colonne 4
# on stocke le résultat dans le dictionnaire totals
# on utilise la méthode astype() pour convertir le type de données de l'array alcohol_column en float
# on utilise la méthode sum() pour calculer la somme des valeurs de l'array alcohol_column

print(totals)