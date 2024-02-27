# create empty dictionary
word_counts = {}

with open('frankenstein.txt', 'r') as text:
	for line in text:		
		words = line.split()
		for word in words:
			# word = clean_word(word) 
			if word in word_counts:
				word_counts[word] = word_counts[word] + 1
			else:
				word_counts[word] = 1

# results = []
# for key in word_counts.keys():
# 	results.append((word_counts[key], key))

# results = [(value, key) for (key, value) in word_counts.items()]

# sorted_results = sorted(results, reverse=True)

# print(sorted_results[:10])

print(sorted(word_counts.items(), key=lambda x:x[1], reverse=True)[0])






