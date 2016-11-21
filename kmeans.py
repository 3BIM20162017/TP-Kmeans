import matplotlib.pyplot as plt
import pandas as pd 
import matplotlib
import numpy as np
matplotlib.style.use('ggplot')

from pandas.tools.plotting import parallel_coordinates
#from pandas.tools.plotting import radviz #(other choice of visualization, if used, uncomment radviz(data, 'Name')


def switch_array(arr):
  """
  Voici une fonction qui peut vous être utile. Elle prend en argument un tableau
  en 2D et renvoie les données en 'inversant' les lignes et colonnes. Ex :
  [[1,2,3],       [[1,4,7],
   [4,5,6],  ==>   [2,5,8],
   [7,8,9]]        [3,6,9]]
   
   Typiquement, si vos données ont des lignes par individus, si vous voulez traiter une liste de
   valeurs présente chez chaque individu (pour faire la moyenne par ex ;) ...) vous pouvez les isoler.
   || Nécessite : import numpy as np ||
  """
  new_arr = np.array([[None]*len(arr)]*len(arr[0]))
  for x, row in enumerate(arr) :
    for y, column in enumerate(row):
      new_arr[y,x] = column

  return new_arr



data = pd.read_csv('iris.csv')
plt.figure()

#radviz(data, 'Name')
parallel_coordinates(data, 'Name')
plt.show()
