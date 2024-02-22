import pandas as pd

food_info = pd.read_csv("food_info.csv")

protein = food_info["Protein_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]

print(protein)
print(cholesterol)