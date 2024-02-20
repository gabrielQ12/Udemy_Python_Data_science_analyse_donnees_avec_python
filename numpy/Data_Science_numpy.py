import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',',dtype="U75", skip_header=1) 

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty, 4] = '0'