import csv
from scipy.stats.stats import pearsonr 
import numpy as np 
import pickle 
from temp import *
import time 

def extract():
	database = []
	f = open("test.csv", "r")
	for row in f:
		row = eval(row)
		database.append([row[1][0], row[1][1], row[2], row[3][0], row[3][1]])
	return database

def column(matrix, i):
	return [row[i] for row in matrix]

def extract2():
	database = extract()
	goldScore = np.asarray(column(database, 2), dtype='float32')
	score1 = np.asarray(column(database, 3), dtype='float32')
	score2 = np.asarray(column(database, 4), dtype='float32')
	return goldScore, score1, score2

def pearsonCorrelation():
	with open('results2.pickle', 'rb') as handle:
		List = pickle.load(handle)
	array = np.asarray(List, dtype='float32')
	#L1, L2 = np.hsplit(array, 0)
	L1, L2 = [float(x[0]) for x in List], [x[1] for x in List]
	L1, L2 = list(L1), list(L2)
	for i in xrange(len(L2)):
		#L2[i] = L2[i][0][0]
		
		try:
			L2[i] = L2[i][0][0]
		except:
			L2[i] = L2[i]
	#print L2, "\n", L1
	#print L2[0][0][0]
	print "Pearson Correlation is: ",pearsonr(L1, L2)[0] 


def load(fileName):
	with open(fileName, "rb") as handle:
		return pickle.load(handle)

def store(fileName, variable):
	with open(fileName, "wb") as handle:
		pickle.dump(variable, handle)

def LinearRegression(Parameter1, Parameter2):
	return [Parameter1[x]*0.61562163+Parameter2[x]*0.29603609 for x in xrange(len(Parameter1))]

def matplot(line1, line2, line3, AuthorAvg, MLAvg):
	#Normalize
	line3 = normalize(line3)
	
	#Plot graph
	import matplotlib.pyplot as plt 
	fig, ax = plt.subplots(nrows = 2, ncols = 1)
	#plt.subplot(2,2,1)
	plt.subplot(2, 1, 1)
	l1 = np.arange(len(line1))
	l2 = np.arange(len(line2))
	
	#plt.subplot(1)
	
	plt.plot(l1, line1)
	plt.plot(l2, line2)
	plt.plot(l2, line3)
	plt.title("Regression")
	plt.legend(["Author's Method", "Proposed Method", "User's Average"])
	#plt.show()
	
	#Bar Chart
	plt.subplot(2, 2, 3)
	top = [('Machine Learning Avg', MLAvg/100), ('Authors Average', AuthorAvg/100)]
	width = 0.7
	labels, values = zip(*top)
	indexes = np.arange(len(labels))
	plt.bar(indexes, values, width)
	plt.xticks(indexes + width *0.5, labels)
	#plt.plot(l2, line2)
	plt.show()


if __name__ == '__main__':
	#pearsonCorrelation()
	#collapse(10)
	score1 = np.asarray(load("term1.pickle"), dtype='float32')
	score2 = np.asarray(load("term2.pickle"), dtype='float32')
	avg = load("Avg.pickle")
	avg = np.asarray(column(avg, 1), dtype='float32')
	mlAvg = np.asarray(LinearRegression(score1, score2), dtype='float32')

	ActualAvg, ActualScore1, ActualScore2 = extract2() 
	#print "Machine Learning Average is ", pearson(avg, ActualAvg)
	#print "Correlation Score between score1 and Actual Score1", pearsonr(score1, ActualScore1)[0]*100, "%"
	#print "Correlation Score between score2 and Actual Score2", pearsonr(score2, ActualScore2)[0]*100, "%"
	print "Correlation Score between Avg and ActualAvg", pearson(mlAvg, ActualAvg)[0]*100, "%"
	print "Correlation Score between ML Avg and Actual Avg", pearson(avg, ActualAvg)[0]*100, "%"
	#print "Correlation Score between mlAvg and avg", pearsonr(mlAvg, avg)[0]*100, "%"
	matplot(avg, mlAvg, ActualAvg, pearson(mlAvg, ActualAvg)[0]*100, pearson(avg, ActualAvg)[0]*100)