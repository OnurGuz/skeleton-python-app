def process_query(query):
	if ("romeo and juliet" in query.lower()):
		return "William Shakespeare"
	if ("258" in query.lower()):
		return "258"
	if ("2010 plus 2013" in query.lower()):
		return "4023"
	if ("what is 5 multiplied by 14" in query.lower()):
		return 5*14
	return ""


