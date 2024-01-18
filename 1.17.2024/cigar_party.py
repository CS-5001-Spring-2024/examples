"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
"""

def cigar_party(cigars: int, is_weekend: bool) -> bool:
	if cigars >= 40 and cigars <= 60:
		return True
	elif cigars >= 40 and is_weekend:
		return True
	return False

def main():
 	# How many tests do we need to do
	# to ensure that our function
	# is correct?
	# we came up with 6 cases in class!
	print(cigar_party(85, True))

if __name__ == '__main__':
	main()