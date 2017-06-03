import re

pattern = re.compile(r'\<.+?\>', re.DOTALL)
def cleanJson(jsonStr):
	return re.sub(pattern, '', jsonStr)

def hashtagPreprocss(text, hashtags):
	hashtag = ''
	for item in hashtags:
		try:
			hashtag += item['text']
		except KeyError:
			continue
	text += hashtag
	return text.lower()