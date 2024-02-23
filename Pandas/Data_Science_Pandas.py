import pandas as pd

food_info = pd.read_csv("food_info.csv")

protein = food_info["Protein_(g)"] *2
fat = food_info["Lipid_Tot_(g)"] * -0.75

rating = protein + fat

print(rating)
