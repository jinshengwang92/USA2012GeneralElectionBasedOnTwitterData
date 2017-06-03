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
	topicFile1 = open (fileName + '_IJ.txt', 'r')
	topicFile2 = open (fileName + '_T.txt', 'r')
	topicFile3 = open (fileName + '_B.txt', 'r')
	topicFile4 = open (fileName + '_P.txt', 'r')
	topicFile5 = open (fileName + '_G.txt', 'r')
	tweetsIJ = ''
	tweetsT = ''
	tweetsB = ''
	tweetsP = ''
	tweetsG = ''

	sentiCounter = SentiCounter()
	print 'IJ'
	sentiCounter.countSentiment(topicFile1)
	print 'T'
	sentiCounter.countSentiment(topicFile2)
	print 'B'
	sentiCounter.countSentiment(topicFile3)
	print 'P'
	sentiCounter.countSentiment(topicFile4)
	print 'G'
	sentiCounter.countSentiment(topicFile5)