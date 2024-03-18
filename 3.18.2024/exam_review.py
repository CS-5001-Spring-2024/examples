# [1, 2, 3, 4, 5]
# [1, 3, 5]

# [8, 8, 8, 8, 5]
# [5]

def no_evens(num_list) -> list:
	if len(num_list) == 0:
		return []
	if num_list[0] % 2 != 0:
		return [num_list[0]] + no_evens(num_list[1:])
	return no_evens(num_list[1:])

# print(no_evens([8, 8, 8, 8, 5]))

"""
 Write a recursive function check_wordle that takes as input a wordle word and a guess and returns the number of green letters -- that is, the number of letters that are the same letter in the same position in both the wordle word and the guess.

 horse
 house
 result -> 4

 snort
 noise
 result -> 0

 spray
 sauce
 result -> 1
"""

def check_wordle(secret, guess) -> int:
	if len(secret) == 0 and len(guess) == 0:
		return 0

	if secret[0] == guess[0]:
		return 1 + check_wordle(secret[1:], guess[1:])
	return check_wordle(secret[1:], guess[1:])

# print(check_wordle('spray', 'sauce'))





'''
9,3,2,4,5,0,0,0,0
0,0,0,0,1,2,3,4,5
'''

board = [
		[9,3,2,4,5,0,0,0,0],
		[0,0,0,0,1,2,3,4,5]
		]

# zero_count = 0

# i = 0
# while i < len(board):
#     j = 0
#     while j < len(board[i]):
#         if board[i][j] == 0:
#             zero_count += 1
#         j += 1
#     i += 1


# # CODE
for list in board: 
	for num in list: 
		if num == 0: 
			zero_count += 1

# print(zero_count)