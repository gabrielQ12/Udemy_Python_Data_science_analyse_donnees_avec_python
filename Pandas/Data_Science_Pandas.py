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