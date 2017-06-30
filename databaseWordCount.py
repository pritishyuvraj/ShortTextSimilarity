import pickle
from nltk.stem import PorterStemmer

with open('database.pickle', 'rb') as handle:
	database = pickle.load(handle)

ps = PorterStemmer()
wordCount = {}
for paragraph in database:
	for word in paragraph:
		word = ps.stem(word[0].lower())
		if word not in wordCount:
			wordCount.setdefault(word, 0)
		else:
			wordCount[word] += 1

with open('wordCount.pickle', 'wb') as handle:
	pickle.dump(wordCount, handle)