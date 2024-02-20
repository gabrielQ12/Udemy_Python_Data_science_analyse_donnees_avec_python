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