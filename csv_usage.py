import csv
import numpy as np      #(optional)

dataset = []

with open('iris.csv','rb') as ir_file:                #open a file
    load = csv.reader(ir_file, delimiter=',')         #use csv, defining the dilimiter
    for row in load :                                 #the csv reader object is run through like an array
      if 0 <=len(row):
        dataset.append(row)                           #append to array
dataset = np.array(dataset)                           #use numpy array for more flexibility

#dataset is now a 2D array containing the data in the csv file.
#you may need to specify the header option if there is a header in your csv file.
# load = csv.reader(ir_file, delimiter=',', header=True)
