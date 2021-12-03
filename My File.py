print("This is word reversing algorithm")
def Name_call():
	sentence = input("Please enter the word to be reversed : ")
	word_counts = { }

	word_counts = sentence.split(' ')

	for x in range(len(word_counts)):
  		word_counts[x] = (word_counts[x])[::-1]

	full_sentence = " ".join(word_counts)
	print(full_sentence)
	Name_call()
Name_call() 

