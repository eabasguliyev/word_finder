words = []
blackList = []
inputBlackList = []

with open('words.txt','r') as f:
	for word in f:
		word = word.replace('\n','')
		words.append(word)

while True:	
	wordInput = input("(quit) >>> ")
	if wordInput in inputBlackList:
		print("This word used.Try again!")
	else:
		inputBlackList.append(wordInput)
		if wordInput == 'quit':
			break
		for word in words:
			if wordInput[-1] == word[0]:
				if word in blackList:
					continue
				else:
					print("Word: {}".format(word))
					blackList.append(word)
					break