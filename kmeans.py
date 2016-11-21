import matplotlib.pyplot as plt
import pandas as pd 
import matplotlib
matplotlib.style.use('ggplot')

from pandas.tools.plotting import parallel_coordinates
#from pandas.tools.plotting import radviz


data = pd.read_csv('iris.csv')
plt.figure()

#radviz(data, 'Name')
parallel_coordinates(data, 'Name')
plt.show()