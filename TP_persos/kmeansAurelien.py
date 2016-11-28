import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

	
class dataset():
	def __init__(self,Nc):
		self.Nc=Nc
		self.D=pd.read_csv("iris.csv",sep=";")
		self.D.columns=["D1","D2","D3","D4","Classe"]
		self.K=pd.DataFrame(np.random.rand(self.Nc,4))
		self.K.columns=["D1","D2","D3","D4"]
		self.K["D1"]=4+4*self.K["D1"]
		self.K["D2"]=2+3*self.K["D2"]
		self.K["D3"]=1+6*self.K["D3"]
		self.K["D4"]=2*self.K["D4"]
		self.K["Classe"] = range(1,self.Nc+1)
		
	def aff(self):
		A=pd.DataFrame(columns=range(1,self.Nc+1))
		for i in range(1,self.Nc+1):
			A[i]=((self.D.iloc[:,0:4]-self.K.iloc[i-1,0:4])**2).sum(1)
		for i in range(0,len(self.D.index)): 
			self.D["Classe"].loc[i]=np.argmin((A).loc[i])
			
	def maj(self):
		for i in range(0,self.Nc):
			if (np.mean(self.D[self.D["Classe"]==(i+1)])).sum()>0:
				self.K.loc[i]=np.mean(self.D[self.D["Classe"]==(i+1)])
			
	def run(self):
		prev=0
		while (self.K.sum(1)).sum()!=prev:
			print(self.K)
			prev=((self.K.sum(1)).sum())
			self.aff()
			self.maj()
		print(self.D)
		print(self.K)
	
	def graph(self):
		l=['bs','rs','gs','cs','ms','ys','ks']
		for i in range(1,self.Nc+1):
			
			plt.subplot(611)
			plt.plot(self.D[self.D["Classe"]==i]["D1"],self.D[self.D["Classe"]==i]["D2"],l[i-1])
			plt.ylabel('D1/D2')
			plt.axis([0,8,0,8])

			plt.subplot(612)
			plt.plot(self.D[self.D["Classe"]==i]["D1"],self.D[self.D["Classe"]==i]["D3"],l[i-1])
			plt.ylabel('D1/D3')
			plt.axis([0,8,0,8])

			plt.subplot(613)
			plt.plot(self.D[self.D["Classe"]==i]["D1"],self.D[self.D["Classe"]==i]["D4"],l[i-1])
			plt.ylabel('D1/D4')
			plt.axis([0,8,0,8])

			plt.subplot(614)
			plt.plot(self.D[self.D["Classe"]==i]["D2"],self.D[self.D["Classe"]==i]["D3"],l[i-1])
			plt.ylabel('D2/D3')
			plt.axis([0,8,0,8])

			plt.subplot(615)
			plt.plot(self.D[self.D["Classe"]==i]["D2"],self.D[self.D["Classe"]==i]["D4"],l[i-1])
			plt.ylabel('D2/D4')
			plt.axis([0,8,0,8])

			plt.subplot(616)
			plt.plot(self.D[self.D["Classe"]==i]["D3"],self.D[self.D["Classe"]==i]["D4"],l[i-1])
			plt.ylabel('D3/D4')
			plt.axis([0,8,0,8])

		plt.show()
		
		
Data=dataset(3)
Data.run()
Data.graph()
