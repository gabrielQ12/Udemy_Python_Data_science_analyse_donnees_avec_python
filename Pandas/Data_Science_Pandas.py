import pandas as pd

food_info = pd.read_csv("food_info.csv")

water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy[0:5])

# ici on multiplie les valeurs de la colonne "Water_(g)" par les valeurs de la colonne "Energ_Kcal" pour chaque ligne
# on obtient un objet Series avec les valeurs résultantes


grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]

print(grams_of_protein_per_gram_of_water)
print("**delimiter**")
print(milligrams_of_calcium_and_iron)

