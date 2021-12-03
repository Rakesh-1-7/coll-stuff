print("This is word reversing algorithm")
def Name_call():
	Text_entered = input("Please enter the word to be reversed : ")
	Text_entered_splitted = Text_entered.split(" ")
	print("Here is your reversed text.")
	Text_entered_joined = ""
	for i in range(len(Text_entered_splitted)):
		
		Text_entered_joined = Text_entered_joined + " " + (Text_entered_splitted[i])[::-1] 
	print(Text_entered_joined)

	Name_call() 


Name_call()
 