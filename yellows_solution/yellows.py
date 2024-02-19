
def check_guess(guess: str, secret: str) -> str:

	result = ['-', '-', '-', '-', '-']
	taken = [False, False, False, False, False]
	i = 0
	while i < len(guess):
		
		if guess[i] == secret[i]:
			# green if same letter, same position
			result[i] = 'G'			
		else:
			j = 0			
			# check whether the current guess letter
			# appears anywhere else in the secret
			while j < len(guess):
				if (
					# The current item of guess is not a green
					i != j
					# The jth item of secret is not a green
					and guess[j] != secret[j]
					# The current item of guess matches the
					# jth item of secret.
					and guess[i] == secret[j] 
					# The jth item of secret has not already
					# been matched to another letter in guess.
					and not taken[j]):
					result[i] = 'Y' # this is a yellow					
					taken[j] = True # and the matching letter in secret is 
									# now taken
					break # don't keep looking
				j += 1		
		i += 1

	return result


print(check_guess('abcde', 'fghij'))
print(check_guess('abcde', 'abcde'))
print(check_guess('abcde', 'abced'))
print(check_guess('aaabb', 'ccaaa'))
print(check_guess('aaabb', 'ccaaa'))
print(check_guess('ccaaa', 'aaabb'))
print(check_guess('aaccc', 'cacac'))
print(check_guess('abcae', 'fghaj'))

