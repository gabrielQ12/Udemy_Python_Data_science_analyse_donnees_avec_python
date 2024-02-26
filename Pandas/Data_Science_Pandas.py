import pandas as pd
import numpy

titanic_survival= pd.read_csv("titanic_survivalcsv")

# si on ajoute (axis=1) a la methode .apply() on applique la fonction a chaque ligne