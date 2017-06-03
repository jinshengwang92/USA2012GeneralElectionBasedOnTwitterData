from config import *

# for ecnomy only 

# topic : (num_good, num_bad)
class SentiCounter(object):
	"""docstring for sentiCount"""
	def __init__(self):
		self.posCount = 0.0
		self.negCount = 0.0
		self.count = 0.0
	'''
	def countSentiment(self, text):
		foundPos = False
		foundNeg = False
		for word in text:
			self.count += 1.0
			if word in pos_words:
				self.posCount += 1.0
			elif word in neg_words:
				self.negCount += 1.0
		# getSupportingRate and print
		total = self.posCount + self.negCount
		print (self.posCount / total, self.negCount / total)	# validate
		print self.count
		self._reset()
	'''

	def countSentiment(self, file):
		foundPos = False
		foundNeg = False
		# total
		num_fav_pos = 0
		num_retweet_pos = 0
		num_fav_neg = 0
		num_retweet_neg = 0
		for line in file:
			line = line.split()
			num_fav = 0
			num_retweet = 0
			try:
				num_fav = int(line[-2][1:-1])
			except (IndexError,ValueError): 
				pass
			try:
				num_retweet = int(line[-1][0:-1])
				#sprint num_retweet
			except (IndexError,ValueError): 
				pass
			self.count += 1.0
			for word in line:
				if word in pos_words:
					self.posCount += 1.0
					num_fav_pos += num_fav
					num_retweet_pos += num_retweet
					# not work
					#self.posCount += (1.0 / (num_fav if num_fav != 0.0 else 1))
					#self.posCount += (1.0 / (num_retweet if num_retweet != 0.0 else 1))
					#self.posCount /= num_retweet if num_retweet != 0.0 else 1
					break
				elif word in neg_words:
					self.negCount += 1.0
					num_fav_neg += num_fav
					num_retweet_neg += num_retweet
					# not work
					#self.negCount += (1.0 / (num_fav if num_fav != 0.0 else 1))
					#self.negCount += (1.0 / (num_retweet if num_retweet != 0.0 else 1))
					#self.negCount /= num_retweet if num_retweet != 0.0 else 1
					break
		# getSupportingRate and print
		self.posCount = self.posCount / num_retweet_pos * num_fav_pos
		self.negCount = self.negCount / num_retweet_neg * num_fav_neg
		total = self.posCount + self.negCount
		print (self.posCount / total, self.negCount / total)	# validated
		print self.count
		self._reset()

	def _reset(self):
		self.posCount = 0.0
		self.negCount = 0.0
		self.count = 0.0