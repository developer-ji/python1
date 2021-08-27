def word_counter(n):
	count = {}
	for i in n:
		count[i] = n.count(i)
	return count
print(word_counter("deependra"))		