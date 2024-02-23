import pandas as pd

food_info = pd.read_csv("food_info.csv")

# score = 2 x protein - 0.75 x lipide 

col_names = food_info.columns.tolist()

sodium_grams = food_info["Sodium_(mg)"] / 1000

sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000

print(sodium_grams)
print(sugar_milligrams)

