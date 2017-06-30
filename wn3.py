from nltk.corpus import wordnet

def returnWordSim(word1, word2):
	word1 = wordnet.synsets(word1)
	word2 = wordnet.synsets(word2)
	if word1 and word2:
		return word1[0].wup_similarity(word2[0])