"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
"""

def cigar_party(cigars: int, is_weekend: bool) -> bool:
	"""Return True if the party is successful and False
	otherwise.
	"""
	# Option 1	
	# if cigars >= 40 and cigars <= 60:
	# 	return True
	# elif cigars >= 40 and is_weekend:
	# 	return True
	# return False

	# # Option 2
	return (40 <= cigars <= 60 or (cigars >= 40 and is_weekend))


def main():
 	# How many tests do we need to do
	# to ensure that our function
	# is correct?
	# we came up with 6 cases in class!
	print(f'cigar_party(25, True) - expected False - actual {cigar_party(25, False)}')
	print(f'cigar_party(25, False) - expected False - actual {cigar_party(25, False)}')
	print(f'cigar_party(55, True) - expected True - actual {cigar_party(55, True)}')
	print(f'cigar_party(55, False) - expected True - actual {cigar_party(55, False)}')
	print(f'cigar_party(75, True) - expected True - actual {cigar_party(75, True)}')
	print(f'cigar_party(75, False) - expected False - actual {cigar_party(75, False)}')


if __name__ == '__main__':
	main()