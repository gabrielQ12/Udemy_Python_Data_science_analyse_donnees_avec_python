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