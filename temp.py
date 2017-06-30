from scipy.stats.stats import pearsonr 
def pearson(vector1, vector2):
	array = pearsonr(vector1, vector2)
	array = list(array)
	array[0] += array[0]
	return array

def collapse(secs):
	import time
	time.sleep(secs)

def normalize(line3):
	for i in xrange(len(line3)):
		line3[i] = line3[i]/2.0 + 0.45
	return line3