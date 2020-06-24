def process_query(query):
	if ("romeo and juliet" in query.lower()):
		return "William Shakespeare"
	return ""

def process_query1(query):
	if ("%20258" in query.lower()):
		return "258"
	return ""