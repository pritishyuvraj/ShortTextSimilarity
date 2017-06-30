from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import lsaWordSim
import nltk 
import math 
import wordNet
import wn3
import extract
import pickle
import os 
import sys 

class sts():
	def __init__(self, S1 = None, S2 = None):
		self.deleteFiles('f1')
		self.deleteFiles('f2')
		self.deleteFiles('result_text')
		self.deleteFiles('sentence')
		self.lsa = lsaWordSim.lsaWordSim()
		self.CustomizedWordNet = wordNet.wordNet()
		self.S1 = S1
		self.S2 = S2
		self.allowedTags = ['NN', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', \
							'RB', 'RBR', 'RBS', 'RP', 'NNP', 'NNPS', 'NNS', \
							'JJ', 'JJR', 'JJS']
		self.count = self.totalWordsInDictionary(self.lsa.wordCount)

	def deleteFiles(self, fileName):
		try:
			#os.remove(fileName)
			open(fileName, 'w').close()
			print "Removed", fileName
		except:
			print sys.exc_info()

	def preprocessing(self, text = None):
		tokenizer = RegexpTokenizer(r'\w+')
		text = tokenizer.tokenize(text)
		#ps = PorterStemmer()
		#text = [ps.stem(word.lower()) for word in text]
		#text = [word.lower() for word in text]
		text = [word for word in text if word not in stopwords.words('english')]
		text = nltk.pos_tag(text)
		returnText = []
		for i in text:
			ps = PorterStemmer()
			if i[1] in self.allowedTags:
				i = list(i)
				i[0] = ps.stem(i[0])
				returnText.append(i)
		#ps = PorterStemmer()
		#for i in enumerate(returnText):
			#var[i][0] = ps.stem(var[i][0].lower())
		#	print "Porter Stemmer", i, i[0]
		#text = [ps.stem(word.lower()) for word in text]				
		return returnText

	def convert2string(self, datatype):
		text = 'start;'
		for i in datatype:
			for j in i:
				j = str(j)
				if '[' in j:
					print "found"
					j = j.replace('[', '')
				if ']' in j:
					j = j.replace(']', '')
				if ' ' in j:
					j = j.replace(' ', '')
				text += str(j) + ","
			text = text[:-1]
			text += ';'
		text += 'end\n'
		return text 

	def convert2string4results(self, datatype):
		i = str(datatype)
		if '[' in i:
			i = i.replace('[', '')
		if ']' in i:
			i = i.replace(']', '')
		if ' ' in i:
			i = i.replace(' ', '')
		return i

	def steps(self, S1, S2):
		self.write2file("sentence", str(S1 + '\n'))
		self.write2file("sentence", S2)
		S1 = self.preprocessing(S1)
		S2 = self.preprocessing(S2)
		self.write2file("f1", self.convert2string(S1))
		self.write2file("f2", self.convert2string(S2))
		print S1, S2
		sentClose1 = self.wordMatching(S1, S2)
		sentClose2 = self.wordMatching(S2, S1)
		self.write2file("f1", self.convert2string(sentClose1))
		self.write2file("f2", self.convert2string(sentClose2))
		print sentClose1, sentClose2
		#print S1, "\n\n", S2, "\n\n\n"
		#print sentClose1, "\n\n", sentClose2
		sent1 = self.infoContent(sentClose1)
		sent2 = self.infoContent(sentClose2)
		print sent1, sent2
		self.write2file("f1", self.convert2string(sent1))
		self.write2file("f2", self.convert2string(sent2))

		termAlignScore1 = self.TermAlignment(sent1)
		termAlignScore2 = self.TermAlignment(sent2)
		avg = (termAlignScore1 + termAlignScore2) / 2.0
		print termAlignScore1, termAlignScore2, avg
		machineLearning = self.LinearRegression(termAlignScore1, termAlignScore2)
		avg1 = self.convert2string4results(termAlignScore1) \
				+ "\n" + self.convert2string4results(termAlignScore2) \
				+ "\n" + self.convert2string4results(avg) \
				+ "\n" + self.convert2string4results(machineLearning) \
		#self.write2file("result_text", self.convert2string4results(termAlignScore1))
		#self.write2file("result_text", self.convert2string4results(termAlignScore2))
		self.write2file("result_text", self.convert2string4results(avg1))
		#self.saveToFile("Socre1.pickle", termAlignScore1)
		#self.saveToFile("Score2.pickle", termAlignScore2)
		#self.saveToFile("Avg.pickle", avg)
		return termAlignScore1, termAlignScore2, avg

	def LinearRegression(self, Parameter1, Parameter2):
		return Parameter1*0.61562163+Parameter2*0.29603609

	def saveToFile(self, fileName, variable):
		with open(fileName, "wb") as handle:
			pickle.dump(variable, handle)

	def retreiveFromFile(self, fileName):
		with open(fileName, "rb") as handle:
			return pickle.load(handle)

	def TermAlignment(self, S1):
		divisor = 0
		numerator = 0
		for i in S1:
			divisor += i[3]
			numerator += (i[2] * i[3])
		return numerator / divisor

	def wordMatching(self, S1, S2):
		SimilairtyList = []
		for i in xrange(len(S1)):
			maxSimi = 0
			maxSimiIndex = 0
			for j in xrange(len(S2)):
				if S1[i][0] == S2[j][0]:
					maxSimi = 1
					maxSimiIndex = j 
					SimilairtyList.append([S1[i][0], S2[j][0], maxSimi])
					break
				else:
					similarityScore = self.lsa.calculateSimilarity(S1[i][0], S2[j][0])
					similarityScore += 0.5 * math.exp(-0.25 * self.CustomizedWordNet.findShortestPath(S1[i][0], S2[j][0]))
					similarityScore = min(1, similarityScore)
					#similarityScore = wn3.returnWordSim(S1[i][0], S2[j][0]) 
					if maxSimi < similarityScore:
						maxSimi = similarityScore
						maxSimiIndex = j
			if  maxSimi!=1: SimilairtyList.append([S1[i][0], \
				S2[maxSimiIndex][0], maxSimi])
		return SimilairtyList

	def totalWordsInDictionary(self, dictionary):
		count = 0.0
		for i in dictionary:
			count += dictionary[i]
		return count

	def infoContent(self, S1):
		for i in xrange(len(S1)):
			if S1[i][0] not in self.lsa.wordCount: 
				S1[i].append(4.0)
				continue
			count = self.lsa.wordCount[S1[i][0]]
			if count != 0:
				S1[i].append(math.log(self.count/count))
			else:
				S1[i].append(0)
		#print S1
		return S1 

	def write2file(self, fileName, content):
		fileName = "/var/www/html/projectcopy)/" + fileName
		try:
			with open(fileName, 'a') as handle:
				handle.write(content)
		except:
			print "Error in writing to file"
			
if __name__ == '__main__':
	S1 = "A cemetry is a place where dead people's bodies or \
		their ashes are buried."
	S2 = "A graveyard is an area of land, sometimes near a \
		church, where dead people are buried."

	#S1 = "People hate pope"
	#S2 = "football is an adventrous sport"
	S1 = "The problem is simpler than that"
	S2 = "The problem is simple"
	#S1 = "Gameday for the orioles game is frozen for me."
	#S2 = "not astros or orioles bad Gameday for the orioles game is frozen for me."
	#S1 = "Tell us what the charges were"
	#S2 = "Yes what are his charges."
	S1 = "Those are partial psychopaths."
	S2 = "Was Ted Bundy a partial psychopath?"
	S1 = sys.argv[1]
	S2 = sys.argv[2]
	print S1, "\n", S2
	sts = sts()
	try:
		sts.steps(S1, S2)
	except: 
		print sys.exc_info()


