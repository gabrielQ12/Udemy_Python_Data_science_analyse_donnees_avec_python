import pandas as pd

import matplotlib.pyplot as plt


unrate = pd.read_csv('unrate.csv') 

# series.dt.month permet de recuperer le mois de la date

# unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(6,6))

plt.plot(unrate[0:12]['MONTH'] , unrate[0:12]['UNRATE'])
plt.plot(unrate[12:24]['MONTH'] , unrate[12:24]['UNRATE'], c='red')

plt.show()
