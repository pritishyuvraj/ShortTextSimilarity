from nltk.stem import WordNetLemmatizer, PorterStemmer
import nltk 
import sys 
import operator
import pickle 
import os 
import math 
import numpy as np 
import time 

class Dict:
	def __init__(self):
		self.fileLoc = open("2+2+3cmn.txt", "r")
		self.allowedTags = ['NN', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', \
							'RB', 'RBR', 'RBS', 'RP', 'NNP', 'NNPS', 'NNS', \
							'JJ', 'JJR', 'JJS']
		self.dictionary = None 
		self.database = None 

	def preProcessing(self, text):
		ps = PorterStemmer()
		if type(text) is not list:
			#print "Single word ", text
			text = ps.stem(text.lower())
			return nltk.pos_tag([text])
		else:
			#print "Multiple Words", text
			text = [ps.stem(word.lower()) for word in text]	
			return nltk.pos_tag(text)

	def parseLines(self, File = None):
		database = []
		dicti = {}
		count = 0
		for i, line in enumerate(File):
			line = line.strip()
			#print line
			try:
				if ',' not in line:
					#Single Word 
					#print "Single Line ", line
					preprocessedWord = self.preProcessing(line)
					#print i, ") Single Line ", line, preprocessedWord
				if ',' in line:
					#Multiple words
					word = line.split(',')
					#print "Multiple Words ", word
					
					word = [w.strip() for w in word]
					preprocessedWord = self.preProcessing(word)
					#print i, ") Multiple Words ", line, preprocessedWord
			except:
				print sys.exc_info()
			else:
				if type(preprocessedWord) is list:
					for w in preprocessedWord:
						if w[0] not in dicti and w[1] in self.allowedTags:
							#unique word
							count += 1
							dicti.setdefault(w[0], count)
							if count != len(dicti):
								print count, len(dicti), w, dicti
								sys.exit()
				else:
					if preprocessedWord[0] not in dicti and preprocessedWord[1]\
					in self.allowedTags:
						#unique word
						count += 1
						dicti.setdefault(preprocessedWord[0], count)
						if count != len(dicti):
							print count, len(dicti), w, dicti	
							sys.exit()
				database.append(preprocessedWord)
		self.dictionary = dicti
		print "Length ", len(self.dictionary)
		try:
			with open('dict.pickle', 'wb') as handle:
				pickle.dump(self.dictionary, handle)
		except:
			print sys.exc_info()
		else:
			print "Saved to the file!!!!!"
		return database, dicti

	def uploadData(self):
		with open('dict.pickle', 'rb') as handle:
			self.dictionary = pickle.load(handle)
		with open('database.pickle', 'rb') as handle:
			self.database = pickle.load(handle)

	def hal(self, window = 1):
		self.uploadData()
		print "process initiated"
		t1 = time.time()
		lenOfMatrix = len(self.dictionary)
		matrix = [[0 for x in xrange(len(self.dictionary))] for y in xrange(len(self.dictionary))]
		print len(matrix), len(matrix[0]), len(self.dictionary)
		#return [0]
		#Parsing the database
		for paragraph in self.database:
			start = 0
			end = len(paragraph)
			for cur, word in enumerate(paragraph):
				start_x = cur - window
				end_y = cur + window + 1
				if start_x < 0: start_x = 0
				if end_y > end: end_y = end
				for checkPos in xrange(start_x, end_y):
					if word[0] == paragraph[checkPos][0]: continue
					#print word[0], paragraph[checkPos][0]
					if word[0] in self.dictionary and\
						paragraph[checkPos][0] in self.dictionary:
						#print self.dictionary[word[0]], self.dictionary[paragraph[checkPos][0]]
						matrix[self.dictionary[word[0]]][self.dictionary[paragraph[checkPos][0]]] += 1
		print "Time taken to process ", (time.time() - t1)/60.0
		t1 = time.time()
		with open('matrix.pickle', 'wb') as handle:
			pickle.dump(matrix, handle)
		print "Time to dump matrix ", (time.time() - t1)/60.0
		return matrix

	def uploadMatrix(self):
		with open('matrix.pickle', 'rb') as handle:
			return pickle.load(handle)

	def logifyTheMatrix(self, matrix = None):
		if matrix is None: 
			start = time.time()
			self.uploadData()
			print ".........Uploaded part 1........"
			matrix = self.uploadMatrix()
			end = time.time()
			print ".....All files uploaded........ time taken", (end-start)/60.0
		t1 = time.time()
		print "......Iterating....."
		for i in xrange(len(matrix)):
			for j in xrange(len(matrix)):
				matrix[i][j] = math.log(matrix[i][j] + 1)
		print "Iteration finished", (time.time() - t1)/60.0
		#self.saveToFile(matrix, "matrixLogged.pickle")	
		print "performing single vector decomposition....."
		t1 = time.time()	
		U, sigma, V = self.randomizedSVD(matrix, 300)
		print "SVD completed.....", (time.time() - t1)/60.0
		self.saveToFile(U, "u.pickle")
		self.saveToFile(sigma, "sigma.pickle")
		self.saveToFile(V, "v.pickle")
		return U, sigma, V
		
	def SVD(self, X):
		P, D, Q = np.linalg.svd(matrix, full_matrices=False)
		matrix_changed = np.dot(np.dot(P, np.diag(D)), Q)
		print (np.std(matrix), np.std(matrix_changed), np.std(matrix - matrix_changed))

	def randomizedSVD(self, X, sigmaNum):
		X = np.array(X, dtype='float32')
		from sklearn.utils.extmath import randomized_svd
		U, sigma, VT = randomized_svd(X, n_components=sigmaNum)
		return U, sigma, VT

	def saveToFile(self, component, fileName):
		with open(fileName, 'wb') as handle:
			pickle.dump(component, handle)
		print ("successfully written to hardDisk")

if __name__ == '__main__':
	dc = Dict()
	print "Starting"
	#database, dictionary = dc.parseLines(dc.fileLoc)
	#dictionary_sorted = sorted(dictionary.items(), key=operator.itemgetter(1))
	#print dictionary_sorted
	'''
	with open('dict.pickle', 'wb') as handle:
		pickle.dump(dictionary, handle)

	
	To upload
	with open('dict.pickle', 'rb') as handle:
		b = pickle.load(handle)
	'''
	matrix = dc.hal(4)
	U, sigma, V = dc.logifyTheMatrix(matrix)