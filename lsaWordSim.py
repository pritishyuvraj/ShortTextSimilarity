from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pickle 
import time
import numpy as np 

class lsaWordSim:
	def __init__(self):
		#self.w1, self.w2 = word1, word2
		print "..........Starting to upload files ......."
		t1 = time.time()
		self.dictionary = self.uploadFiles("dict.pickle")
		self.U = self.uploadFiles("u.pickle")
		self.sigma = self.uploadFiles("sigma.pickle")
		self.V = self.uploadFiles("v.pickle")
		self.wordCount = self.uploadFiles("wordCount.pickle")
		print "All files successfully uploaded..........", (time.time() - t1)

	def uploadFiles(self, fileName):
		with open(fileName, 'rb') as handle:
			return pickle.load(handle)	

	def preProcessing(self, word):
		ps = PorterStemmer()
		return ps.stem(word.lower())

	def checkWordPresence(self, w1 = None, w2 = None):
		if w1 is None or w2 is None: w1, w2 = self.w1, self.w2
		if w1 in self.dictionary and w2 in self.dictionary:
			return self.dictionary[w1], self.dictionary[w2]
		else:
			return -1, -1

	def uSigma(self, index):
		vector = []
		row = self.U[index]
		for i in xrange(len(row)):
			vector.append(row[i] * self.sigma[i])
		vector = np.asarray(vector, dtype='float32')
		return vector

	def sigmaV(self, index):
		vector = []
		for i in xrange(len(self.sigma)):
			vector.append(self.sigma[i] * self.V[i][index])
		vector = np.asarray(vector, dtype='float32')
		return vector

	def calculateSimilarity(self, w1 = None, w2 = None):
		self.w1 = self.preProcessing(w1)
		self.w2 = self.preProcessing(w2) 
		index_w1, index_w2 = self.checkWordPresence()
		if index_w1 != -1 and index_w2 != -1:
			#print "Both words found in the dictionary"
			vector1 = self.uSigma(index_w1)
			vector2 = self.sigmaV(index_w2)
			similarityScore = cosine_similarity([vector1], [vector2])
			return similarityScore
		else:
			#print "Both words not found in the dictionary"
			return 0

if __name__=='__main__':
	lsa = lsaWordSim("person", "car")
	#print lsa.checkWordPresence()
	print lsa.calculateSimilarity()