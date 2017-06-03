#economyTopics = [['income', 'job','employ'], ['tax'], ['budget', 'deficit']]
#healthTopics = ['medi', 'cover', 'heal', 'hosp']
#safetyTopics = []
def extractTopic(text):
	# economy
	if 'income' in text \
		or 'job' in text \
		or 'employ' in text \
		or 'hire' in text \
		or 'business' in text \
		or 'bankrupt' in text:
		return 'IJ'  #income and jobs

	elif 'tax' in text \
		or 'ira' in text:
		return 'T'  # tax

	elif 'budget' in text \
		or 'debt' in text \
		or 'deficit' in text:
		return 'B' # budget

	elif 'hous' in text \
		or 'liv' in text \
		or 'Fannie Mae' in text \
		or 'Freddie Mac' in text \
		or 'loan' in text \
		or 'mortgag' in text \
		or 'welfar' in text:
		return 'P'  # peopleliving and housing

	elif 'wallstreet' in text \
		or 'stock' in text \
		or 'market' in text \
		or 'trad' in text \
		or 'exchange rat' in text \
		or 'stimulu' in text \
		or 'rescue plan' in text \
		or 'infrastructur' in text \
		or 'econom' in text:
		return 'G'  #great economy related

	else:
		return None

#end def extractTopic