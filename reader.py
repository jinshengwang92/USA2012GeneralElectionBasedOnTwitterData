from StringIO import StringIO
from zipfile import ZipFile
import urllib2
import gzip
import re
import json
import socket
import time

from config import *
from topic import *
from candidateFilter import *
from sentimentPMI import *
from helper import *

num_of_retries = 50
# tweetRomneyTotal = open('tweetRomneyT'+'.txt', 'w')
# tweetRomneyCount = open('tweetRomneyCount.txt', 'w')
tweetFL = open('tweetFL.txt', 'w')
tweetIA = open('tweetIA.txt', 'w')
tweetVA = open('tweetVA.txt', 'w')
tweetOH = open('tweetOH.txt', 'w')
tweetCO = open('tweetCO.txt', 'w')
i = 0
for fileStr in fileStrs: #reversed(fileStrs[:i]):
	# url is a file-like object
	url = None
	for _ in range (num_of_retries):
		try:
			url = urllib2.urlopen(fileStr, timeout = 50)
			print 'Success open: ' + fileStr
			break
		except urllib2.URLError:
			time.sleep(5)

	tic = time.time()

	try:
		gzipfile = gzip.GzipFile(fileobj = StringIO(url.read()))
	except IOError:
		print 'Error read: ' + fileStr
		continue

	toc = time.time()
	print toc - tic
	# tweetRomney = open('tweetRomney'+str(i)+'.txt', 'w')
	i -= 1
	tweetCount = 0

	for jsonStr in gzipfile:
		jsonStrClean = cleanJson(jsonStr)
		#print jsonStrClean
		try:
			jsonDict = json.loads(jsonStrClean)
		except:
			continue

		text = ''
		try:
			text = jsonDict['text']
		except KeyError:
			pass
		hashtags = []
		try:
			hashtags = jsonDict['entities']['hashtags']
		except KeyError:
			pass
		location = ''
		try:
			location = jsonDict['user']['location']
			if location == '':
				continue
		except KeyError as e:
			continue
		try:
			lang = jsonDict['user']['lang']
			if lang != '' and lang != 'en':
				continue
		except KeyError as e:
			continue
		num_fav = 0
		try:
			num_fav = jsonDict['user']['favourites_count']
			if lang != '':
				num_fav = int(num_fav)
		except KeyError as e:
			pass
		num_retweet = 0
		try:
			num_retweet = jsonDict['retweet_count']
			if num_retweet != '':
				num_retweet = int(num_retweet)
		except KeyError as e:
			pass

		text = hashtagPreprocss (text, hashtags)
		if text == '':
			continue
		text += str((num_fav,num_retweet)) + '\n'

		if not aboutRomney(text):
			continue

		if location in FL:
			tweetFL.write(text.encode('utf8'))
		if location in IA:
			tweetIA.write(text.encode('utf8'))
		if location in VA:
			tweetVA.write(text.encode('utf8'))
		if location in OH:
			tweetOH.write(text.encode('utf8'))
		if location in CO:
			tweetCO.write(text.encode('utf8'))

		#tweetCount += 1
	#tweetRomneyCount.write(str(tweetCount))
	print 'finished ' + str(fileStr)