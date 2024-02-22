import pandas as pd

food_info = pd.read_csv("food_info.csv")

row_100 = food_info.loc[99]

# ici on a affiché la 100ème ligne du dataframe food_info

print(row_100)