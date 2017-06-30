#https://wordnet.princeton.edu/man/wngloss.7WN.html
from nltk.corpus import wordnet as wn 

class wordNet:
	def __init__(self):
		pass 

	def step1(self, word1, word2):
		#They are in the same WordNet synset
		#http://stackoverflow.com/questions/28818569/how-compare-wordnet-synsets-with-another-word
		for s in wn.synsets(word1):
			lemmas = s.lemmas()
			for l in lemmas:
				if l.name() == word2:
					return 0
		return 3

	def step2(self, word1, word2):
		#One word is the direct hypernym of the other
		#http://stackoverflow.com/questions/26222484/determining-hypernym-or-hyponym-using-wordnet-nltk
		word1 = wn.synsets(word1)[0]
		hypoWord1 = [i for i in word1.closure(lambda s:s.hyponyms())]
		#print hypoWord1
		for l in hypoWord1:
			for l1 in l.lemmas():
				if l1.name() == word2:
					return 1
		return 3		

	def step3(self, word1, word2):
		#One word is the two-link indirect hypernym of the other
		indirectHyponym = []
		word1 = wn.synsets(word1)[0]
		hypoWordLevel1 = [i for i in word1.closure(lambda s:s.hyponyms())]
		for level1 in hypoWordLevel1:
			level1 = level1.name().split('.')[0]
			level1 = wn.synsets(level1)[0]
			level1hypoWords = [i for i in level1.closure(lambda s:s.hyponyms())]
			for l in level1hypoWords:
				for l1 in l.lemmas():
					indirectHyponym.append(l1.name().lower())
		if word2 in indirectHyponym:
			return 2
		return 3

	def step4(self, word1, word2):
		#One adjective has a direct similar to relation with the other
		adjWord1 = wn.synsets(word1)
		adj1 = []
		for i in adjWord1:
			adj = i.name().split('.')
			if adj[1] == 'a':
				adj1.append(adj[0])
		adjWord2 = wn.synsets(word2)
		adj2 = []
		for i in adjWord2:
			adj = i.name().split('.')
			if adj[1] == 'a':
				adj2.append(adj[0])
		common = list(set(adj1).intersection(adj2))
		if common:
			return 1
		return 3

	def step5(self, word1, word2):
		#One adjective has a two-link indirect similar to relation with the other
		adjword1 = wn.synsets(word1)
		adj1 = []		

	def step6(self, word1, word2):
		if word1 == word2:
			return 1
		return 3

	def findShortestPath(self, word1, word2):
		try:
			List = []
			List.append(self.step1(word1, word2))
			List.append(self.step1(word2, word1))
			List.append(self.step2(word1, word2))
			List.append(self.step2(word2, word1))
			List.append(self.step3(word1, word2))
			List.append(self.step3(word2, word1))
			List.append(self.step4(word1, word2))
			List.append(self.step4(word2, word1))
			List.append(self.step6(word1, word2))
			mini = min(List)
			if mini < 3:
				print mini
				return mini
			return 100
		except:
			return 100		
		
if __name__ == '__main__':
	WN = wordNet()
	#print WN.step1("cat", "kat")
	#print WN.step2("math", "wine")
	#print WN.step3("math", "esr")
	#print WN.step4("most", "pritish")
	print WN.findShortestPath("animal", "cat")
