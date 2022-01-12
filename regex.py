#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re
from os import listdir
from os.path import isfile, join

def does_file_exist_in_dir(path):
    return any(isfile(join(path, i)) for i in listdir(path))

def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))


def createUser():
	f = open("loginNames.txt","rw+")

def promptUser():
	username = raw_input("Username: ")
	password = raw_input("Password: ")
	return username, password

def main():
	# Ask for a username
	# Ask for a password
	username,password = promptUser()
 	# Open file and get usernames
 	# open file and get passwords (put them in dictionary)
 	# check keys for a match
 	# if key has a match then check password
 	# if doesn't have a match, try again or create user

main()

