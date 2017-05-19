#Allows lines to be broken up into tokens by using regex
from nltk.tokenize import RegexpTokenizer
#Regex
import re
import sys

#Given a gcode line
#Return an array of tokens following the described regex rules
def lexer(textLine):

	pattern = ""
	#pattern += "G69.*|G\d+" #G word
	#pattern += "|M\d+" #M word
	pattern += "V\d+" #Variable rule
	pattern += "|\d+\.?\d*" #numbers rule
	pattern += "|[+-/*=()]" #Operations rule

	tokenizer = RegexpTokenizer(pattern)
	tokens = tokenizer.tokenize(textLine)

	#Add a newline if no tokens to maintain spacing
	if(len(tokens) == 0):
		tokens.append("\n")
	return tokens