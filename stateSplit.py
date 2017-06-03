'''
tweetRomneyFL = open('tweetRomneyT'+'.txt', 'w')
tweetRomneyVA = open('tweetRomneyT'+'.txt', 'w')
tweetRomneyOH = open('tweetRomneyT'+'.txt', 'w')
tweetRomneyCO = open('tweetRomneyT'+'.txt', 'w')
tweetRomneyOH = open('tweetRomneyT'+'.txt', 'w')
'''

for i in range (1, 34):
	tweetRomney = open('tweetRomney'+str(i)+'.txt', 'r')
	tweets = tweetRomney.read()
	