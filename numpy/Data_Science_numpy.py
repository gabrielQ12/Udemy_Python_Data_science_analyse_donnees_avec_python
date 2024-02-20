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






