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
class sts():
	def __init__(self, S1 = None, S2 = None):
		self.lsa = lsaWordSim.lsaWordSim()
		self.CustomizedWordNet = wordNet.wordNet()
		self.S1 = S1
		self.S2 = S2
		self.allowedTags = ['NN', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', \
							'RB', 'RBR', 'RBS', 'RP', 'NNP', 'NNPS', 'NNS', \
							'JJ', 'JJR', 'JJS']
		self.count = self.totalWordsInDictionary(self.lsa.wordCount)

	def preprocessing(self, text = None):
		tokenizer = RegexpTokenizer(r'\w+')
		text = tokenizer.tokenize(text)
		ps = PorterStemmer()
		text = [ps.stem(word.lower()) for word in text]
		#text = [word.lower() for word in text]
		text = [word for word in text if word not in stopwords.words('english')]
		text = nltk.pos_tag(text)
		returnText = []
		for i in text:
			if i[1] in self.allowedTags:
				returnText.append(i)
		return returnText

	def steps(self, S1, S2):
		S1 = self.preprocessing(S1)
		S2 = self.preprocessing(S2)
		print S1, S2
		sentClose1 = self.wordMatching(S1, S2)
		sentClose2 = self.wordMatching(S2, S1)
		print sentClose1, sentClose2
		#print S1, "\n\n", S2, "\n\n\n"
		#print sentClose1, "\n\n", sentClose2
		sent1 = self.infoContent(sentClose1)
		sent2 = self.infoContent(sentClose2)
		print sent1, sent2
		termAlignScore1 = self.TermAlignment(sent1)
		termAlignScore2 = self.TermAlignment(sent2)
		avg = (termAlignScore1 + termAlignScore2) / 2.0
		print termAlignScore1, termAlignScore2, avg
		#self.saveToFile("Socre1.pickle", termAlignScore1)
		#self.saveToFile("Score2.pickle", termAlignScore2)
		#self.saveToFile("Avg.pickle", avg)
		return termAlignScore1, termAlignScore2, avg

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

if __name__ == '__main__':
	matrix = []
	sts = sts()
	termAlignScore1 = []
	termAlignScore2 = []
	database = extract.extract()
	for i in database:
		print i
		term1, term2, value = sts.steps(i[0], i[1])
		matrix.append([i[2], value])
		termAlignScore1.append(term1)
		termAlignScore2.append(term2)
	print matrix
	sts.saveToFile("term1.pickle", termAlignScore1)
	sts.saveToFile("term2.pickle", termAlignScore2)
	sts.saveToFile("avg.pickle", matrix)
	#with open('results2.pickle', 'wb') as handle:
	#	pickle.dump(matrix, handle)















'''
	S1 = "A cemetry is a place where dead people's bodies or \
		their ashes are buried."
	S2 = "A graveyard is an area of land, sometimes near a \
		church, where dead people are buried."

	#S1 = "People hate pope"
	#S2 = "football is an adventrous sport"
	S1 = "The problem is simpler than that"
	S2 = "The problem is simple"
	S1 = "Gameday for the orioles game is frozen for me."
	S2 = "not astros or orioles bad Gameday for the orioles game is frozen for me."
	S1 = "Tell us what the charges were"
	S2 = "Yes what are his charges."
	S1 = "Those are partial psychopaths."
	S2 = "Was Ted Bundy a partial psychopath?"
	#sts = sts()
	#sts.steps(S1, S2)
'''

