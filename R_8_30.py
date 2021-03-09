"""R-8.30 The build expression tree method of the ExpressionTree class requires
input that is an iterable of string tokens. We used a convenient exam-
ple, (((3+1)x4)/((9-5)+2)) , in which each character is its own to-
ken, so that the string itself sufficed as input to build expression tree.
In general, a string, such as (35 + 14) , must be explicitly tokenized
into list [ ( , 35 , + , 14 , ) ] so as to ignore whitespace and to
recognize multidigit numbers as a single token. Write a utility method,
tokenize(raw), that returns such a list of tokens for a raw string."""

def tokenize(raw):
	"""Tokenize a mathematical expression in order to build Expression tree
	Remove white space and tokenize multidigit numbers into a  single token"""
	
	data = raw.replace(' ', '')  # remove white space
	new = []
	start = 0
	while start < len(data):
		# In case of multidigit numbers, initialise a temporary list 
		# as a storage and append each digit. Join as a single token
		# and append to our new list
		if data[start].isdigit():		
			current = start				# start from the current digit
			temp = []
			# Progress until reach an operator or reach the end of the string
			while current < len(data) and data[current].isdigit(): 
				temp.append(data[current])
				current += 1
			new.append(''.join(temp))
			start = current		# next index is the one after current 
		else:
			new.append(data[start])
			start += 1
		
	return new
	
	
	
		
			
