letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
numbers = "1 2 3 4 5 6 7 8 9"
letters = letters.split(" ")
u_input = raw_input("Enter the phrase to be encrypted")
u_input.lower()
def encrypt(u_input):
	lengthofinput=len(u_input)
	newword=[]
	for letter in u_input:
		if letter == "z":
			newword.append("a")
		elif letter not in letters:
			if letter in numbers:
				if int(letter) + 1 == 10:
					newword.append("0")
				else:
					newword.append(int(letter) + 1)
		else:
			counter = 0
			for alpha_letter in letters:
				if letter == alpha_letter:
					new_letter = letters[counter+1]
					newword.append(new_letter)
				counter += 1




	print newword

encrypt(u_input)

def decrypt (u_input):

	lengthofinput=len(u_input)
	newword=[]
	for letter in u_input:
		if letter == "a":
			newword.append("z")
		elif letter not in letters:
			if letter in numbers:
				if int(letter) == 0:
					newword.append("9")
				else:
					newword.append(int(letter) - 1)
		else:
			counter = 1
			for alpha_letter in letters:
				if letter == alpha_letter:
					new_letter = letters[counter-1]
					newword.append(new_letter)
				counter += 1

	print newword 


decrypt(u_input)


restart = input ("would you like to do this agin: ")
if (restart == "yes"):
	print ("ok")
	encrypt(u_input)
	decrypt(u_input)
else 
	print("ok")
