import sys
import re
#Custom iterator class for tokenSortRecur
class tokenIter:
	#Init
	def __init__(self, tokens):
		self.tokens = tokens
		self.i = -1

    #Without moving the iterator, return the next token's value
    #If out of bounds, return None
	def peek(self):
		if(self.i + 1 < len(self.tokens)):
			return self.tokens[self.i + 1]
		else:
			return None

	#Move the iterator to the next non BinaryOp token
	#Also combines token with the previous if it was a negative sign and not subtraction
	def parsePrimary(self):
		#If we're already on a non-BinaryOp token, then the loop won't increment
		#To get the NEXT non-BinaryOp token, increment by one
		self.i += 1

		#Look until the token is not a BinaryOp
		while(isBinaryOp(self.tokens[self.i])):
			self.i += 1

		#At this point we have a non-BinaryOp
		#Check to see if previous element was a "-" sign
		if(self.tokens[self.i-1] == "-"):
			#Then check token before that one to see if this is supposed to be a negative sign

			#If nothing before it, then it's a negative
			if(self.i - 2 < 0):
				print("List too small!")
				#Combine current token with previous negative sign
				return "-" + self.tokens[self.i]
			elif(isBinaryOp(self.tokens[self.i-2])):
				#Combine current token with previous negative sign
				print("Is a negative!")
				return "-" + self.tokens[self.i]
		
		return self.tokens[self.i]

	#Return current location's token, for debugging
	def location(self):
		return self.tokens[self.i]

#Takes an array of tokens and stores it into the datastructure
def parser(tokens):
	
	next_tok = next(tokens)

	if next_tok.isdigit():
		return ('literal', next_tok)
	elif next_tok == "+":
		return ('add', parse( tokens ), parse( tokens )) # first argument is the node.left, second is the node.right
	elif next_tok == "-":
		return ('sub', parse( tokens ), parse( tokens ))
	elif next_tok == "*":
		return ('mul', parse( tokens ), parse( tokens ))
	elif next_tok == "//":
		return ('div', parse( tokens ), parse( tokens ))
	else:
		return ('variable', next_tok)

#Helper function for tokenSortRecur
#Given a token, return true if it is a basic binary operator
def isBinaryOp(token):
	ret = re.search("[*|/|+|=|-]", token)
	if(ret == None):
		return False
	return True

#Helper function for tokenSortRecur
#Given a token, return the its precedence
#The numbers establish precedence but are arbitrary
def precedenceLookUp(token):
	if(token == "(" or token == ")"):
		return 30
	elif(token == "*" or token == "/"):
		return 25
	elif(token == "+" or token == "-"):
		return 20
	elif(token == "="):
		return 10
	else:
		return 0

#Helper function for tokenSortRecur
#Boolean function that returns true if tokenOne as high associativity than tokenTwo
def isRightAssociative(tokenOne, tokenTwo):
	if(tokenOne == "+" and tokenTwo == "-"):
		return True
	elif(tokenOne == "*" and tokenTwo == "/"):
		return True
	elif(tokenOne == "(" and tokenTwo == ")"):
		return True

	return False

#Helper function for tokenSortRecur
#Given the operator, left-hand-side, and right-hand-side
#Return a single array
#The left-hand-side and right-hand-side can be either arrays or a string
def combine(op, lhs, rhs):
	print("combine" + str(op) + " " + str(lhs) + " " + str(rhs))
	result = [op]
	if(type(lhs) is list):
		result += lhs
	else:
		result.append(lhs)

	if(type(rhs) is list):
		result += rhs
	else:
		result.append(rhs)
	return result

#Recursive function of tokenSort
def tokenSortRecur(lhs, min_prec, iterator):
	#print("lhs: " + str(lhs) + " min_prec: " + str(min_prec))
	#Peek at next token
	lookAhead = iterator.peek()
	print("lookAhead1: " + str(lookAhead))
	#While the next token is not None, has a precedence >= min_prec, and is a binary operation
	while(lookAhead is not None and precedenceLookUp(lookAhead) >= min_prec and isBinaryOp(lookAhead)):
		#Store the next token
		op = lookAhead
		print("op:" + str(lookAhead))
		#rhs = the next non-binary token
		#If the previous token was a - sign, and the token before that was an operation
		#rhs will be negative
		#ex: ["V1", "=", "-", "10"]
		#If the iterator is at 10, it will combine it with the previous token return to return "-10" 
		rhs = iterator.parsePrimary()

		#Parenthesis check
		#If a parenthesis is detected then recurse on the inner experession of the parenthesis
		if(rhs == "("):
			#lhs of the inner parenthesis
			recurLHS = iterator.parsePrimary()
			#Recurse
			rhs = tokenSortRecur(recurLHS , 0, iterator)
			print("Parenthesis case: " + str(rhs))

			#print("Iterator location " + str(iterator.location()))
			#Iterator onto right parenthesis
			iterator.parsePrimary()
			#print("Iterator location " + str(iterator.location()))

			#Append parenthesis around both sides
			rhs.insert(0, "(")
			rhs.append(")")

		print("rhs: " + str(rhs))
		#Peek at next token
		lookAhead = iterator.peek()
		print("lookAhead2: " + str(lookAhead))

		#Calculate precedence of op and lookAhead

		#If lookAhead is not None and (is a binary Op and has a higher precedense than op)
		#OR (lookAhead has the same precedence as OP and is right associative)
		while(lookAhead is not None and (isBinaryOp(lookAhead) and (precedenceLookUp(lookAhead) > precedenceLookUp(op)) ) or
			(isRightAssociative(lookAhead, op) and (precedenceLookUp(lookAhead) == precedenceLookUp(op))) ):

			#Recurse on the right-hand-side
			print("Reccuring with rhs: " + str(rhs) + " lookAheadPrec: " + str(precedenceLookUp(lookAhead)))
			rhs = tokenSortRecur(rhs, precedenceLookUp(lookAhead), iterator)
			print("Returned rhs is: " + str(rhs))
			#Peek at the next token
			lookAhead = iterator.peek()
			print("lookAhead3:" + str(lookAhead))

		#Combine the operator, left-hand-side, and right-hand-side into a single array
		lhs = combine(op, lhs, rhs)
		print("returning: " + str(lhs))
	return lhs

#Given the tokens from the lexer
#Return the tokens arranged in order of precedence and associativity
def tokenSort(tokens):
	print("\n\nTokenSort: ")
	iterator = tokenIter(tokens)
	print(tokens)
	return tokenSortRecur(iterator.parsePrimary(), 0, iterator)