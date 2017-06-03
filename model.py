from topic import *
from candidateFilter import *
from sentimentPMI import *
from helper import *
from config import *

states = ['FL', 'IA', 'VA', 'OH', 'CO']

dir = 'test/'

for state in states:
	print state
	fileName = dir + 'tweet' + state 
	tweetFile = open(fileName + '.txt', 'r')
	topicFile1 = open (fileName + '_IJ.txt', 'w')
	topicFile2 = open (fileName + '_T.txt', 'w')
	topicFile3 = open (fileName + '_B.txt', 'w')
	topicFile4 = open (fileName + '_P.txt', 'w')
	topicFile5 = open (fileName + '_G.txt', 'w')
	tweetsIJ = ''
	tweetsT = ''
	tweetsB = ''
	tweetsP = ''
	tweetsG = ''

	for line in tweetFile:
		topic = extractTopic(line)
		if topic is None:
			continue
		if topic == 'IJ':
			topicFile1.write(line)
			tweetsIJ += line
		elif topic == 'T':
			topicFile2.write(line)
			tweetsT += line
		elif topic == 'B':
			topicFile3.write(line)
			tweetsB += line
		elif topic == 'P':
			topicFile4.write(line)
			tweetsP += line
		elif topic == 'G':
			topicFile5.write(line)
			tweetsG += line

	sentiCounter = SentiCounter()
	print 'IJ'
	sentiCounter.countSentiment(tweetsIJ.split())
	print 'T'
	sentiCounter.countSentiment(tweetsT.split())
	print 'B'
	sentiCounter.countSentiment(tweetsB.split())
	print 'P'
	sentiCounter.countSentiment(tweetsP.split())
	print 'G'
	sentiCounter.countSentiment(tweetsG.split())

	tweetFile.close()