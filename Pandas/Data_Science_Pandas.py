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