from queryprocessor import process_query

def test_knows_who_wrote_romeo_and_juliet():
	assert process_query("Who wrote Romeo and Juliet") == "William Shakespeare"

def test_is_case_insensitive():
	assert process_query("Who wrote romeo and JULIET") == "William Shakespeare"

def test_returns_empty_string_if_cannot_process_query():
	assert process_query("xxxx") == ""

def test_largest_number_between_258_and_87():
	assert process_query("which of the following numbers is the largest: 258, 87") == "258"

def test_largest_number_between_65_and_555_and_51_and_989():
	assert process_query("which of the following numbers is the largest: 65 and 555 and 51 and 989") == "989"
