import numpy as np

# Fonction numpy pour afficher les données

wordl_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1)

## ici U75 est le type de données que nous voulons pour notre tableau numpy cela correspond à des chaines de caractères de 75 caractères maximum

print(wordl_alcohol) 


