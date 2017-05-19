
#Import parser
import sys

#Import lexer
from lexer import lexer
#Import parser
from tokenparser import parser, tokenSort

#Import test cases
from unitTester import lexerBasicTestSuite, lexerMinusSignTestSuite, allLexerTests, allTokenSortTests


#Test lexer
#allLexerTests()
allTokenSortTests()

sys.exit(0)

#testLexer()
#sys.exit(0)
fileName = "testInput/variables.nc"

f = open(fileName, 'r')

line = f.readline()
while line:
	#Break the line into an array of tokens following the language's rules
	tokens = lexer(line)
	#print(len(tokens))
	print(tokens)
	#Parse the tokens into a nested tree
	tree = parse(iter(tokens))

	print("\nTree:" + str(tree))
	line = f.readline()


