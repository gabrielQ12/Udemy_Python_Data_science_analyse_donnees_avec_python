import pandas as pd

food_info = pd.read_csv("food_info.csv")



max_calories = food_info["Energ_Kcal"].max() 



normalized_calories = food_info["Energ_Kcal"] / max_calories
print(normalized_calories)

normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()

food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat

print(food_info.head())