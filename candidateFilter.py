# for Romney
keywords = ['romney', 'mitt', 'paul ryan', 'believe in america', 'believeinamerica', 'republic']


def aboutRomney(text):
	for keyword in keywords:
		if keyword in text:
			return True
	else:
		return	False