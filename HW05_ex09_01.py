#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body

def read_file():
	fp = open("words.txt", "r")
	lines = fp.readlines()
	
	for word in lines:
		word_no_space = word.strip()
		
		if len(word_no_space) > 20:
			print(word_no_space)



##############################################################################
def main():
    read_file()  # Call your functions here.

if __name__ == '__main__':
    main()
