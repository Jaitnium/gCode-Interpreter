#Used for testing cases
import unittest

#Import lexer
from lexer import lexer
#Import Parser and tokenSort
from tokenparser import parser, tokenSort
import sys


class lexerBasicTestCases(unittest.TestCase):
	#Basic operations
	#Basic operations 
	    #(*/+-)
	    #Increasing number of numbers
	    #Change spacing
	    #Incorporate variables
	    #Try parenthesis, then nested parenthesis
	    #Test negatives

    #Test using positive numbers, and basic operations (except "-")
	def Test1(self):
		test = "9+4"
		output = ["9", "+", "4"]
		self.assertEqual(lexer(test), output)	
	def Test2(self):
		test = "9 + 4"
		output = ["9", "+", "4"]
		self.assertEqual(lexer(test), output)	
	def Test2(self):
		test = "9    +  4"
		output = ["9", "+", "4"]
		self.assertEqual(lexer(test), output)	
	def Test3(self):
		test = "9+ 4"
		output = ["9", "+", "4"]
		self.assertEqual(lexer(test), output)
	def Test4(self):
		test = "9 +4"
		output = ["9", "+", "4"]
		self.assertEqual(lexer(test), output)
	def Test5(self):
		test = "3*4"
		output = ["3", "*", "4"]
		self.assertEqual(lexer(test), output)	
	def Test6(self):
		test = "3.999 * 4"
		output = ["3.999", "*", "4"]
		self.assertEqual(lexer(test), output)	
	def Test7(self):
		test = "3   *     4"
		output = ["3", "*", "4"]
		self.assertEqual(lexer(test), output)	
	def Test8(self):
		test = "3* 4"
		output = ["3", "*", "4"]
		self.assertEqual(lexer(test), output)	
	def Test9(self):
		test = "3 *4.23"
		output = ["3", "*", "4.23"]
		self.assertEqual(lexer(test), output)	
	def Test10(self):
		test = "15/3"
		output = ["15", "/", "3"]
		self.assertEqual(lexer(test), output)	
	def Test11(self):
		test = "14 * 8.23 / 9.5 + 3"
		output = ["14", "*", "8.23", "/", "9.5", "+", "3"]
		self.assertEqual(lexer(test), output)	
	def Test12(self):
		test = "10.111 / 10.2322 *914*     0.1"
		output = ["10.111", "/", "10.2322", "*", "914", "*", "0.1"]
		self.assertEqual(lexer(test), output)	
	def Test13(self):
		test = "103.249*0.14+0-1/99/1+8"
		output = ["103.249", "*", "0.14", "+", "0", "-", "1", "/", "99", "/", "1", "+", "8"]
		self.assertEqual(lexer(test), output)	

#Using Variables, basic operations, numbers, and varying spacing
#Ensure that a minus sign is always treated the same
class lexerMinusSignTestCases(unittest.TestCase):

	def Test1(self):
		test = "V1=-4"
		output = ["V1", "=", "-", "4"]
		self.assertEqual(lexer(test), output)	
	def Test2(self):
		test = "V1 = -4"
		output = ["V1", "=", "-", "4"]
		self.assertEqual(lexer(test), output)	
	def Test3(self):
		test = "V1 = -  4"
		output = ["V1", "=", "-", "4"]
		self.assertEqual(lexer(test), output)
	def Test4(self):
		test = "V1=10-4"
		output = ["V1", "=", "10", "-", "4"]
		self.assertEqual(lexer(test), output)
	def Test5(self):
		test = "V1=10 - 4"
		output = ["V1", "=", "10", "-", "4"]
		self.assertEqual(lexer(test), output)
	def Test6(self):
		test = "V1=10 - 4"
		output = ["V1", "=", "10", "-", "4"]
		self.assertEqual(lexer(test), output)
	def Test7(self):
		test = "V1=-V2"
		output = ["V1", "=", "-", "V2"]
		self.assertEqual(lexer(test), output)
	def Test8(self):
		test = "V1= - V2"
		output = ["V1", "=", "-", "V2"]
		self.assertEqual(lexer(test), output)
	def Test9(self):
		test = "V1=10 - V2"
		output = ["V1", "=", "10", "-", "V2"]
		self.assertEqual(lexer(test), output)
	def Test10(self):
		test = "V1 = -  V2 + -9 * 4"
		output = ["V1", "=", "-", "V2", "+", "-", "9", "*", "4"]
		self.assertEqual(lexer(test), output)
	def Test11(self):
		test = "-10 / 2 * -10 + 4"
		output = ["-", "10", "/", "2", "*", "-", "10", "+", "4"]
		self.assertEqual(lexer(test), output)	
	def Test12(self):
		test = "V1 = -V2 - V9 - - V9 * -  4.23"
		output = ["V1", "=", "-", "V2", "-", "V9", "-", "-", "V9", "*", "-", "4.23"]
		self.assertEqual(lexer(test), output)	

#Test parenthesis and nested parentehsis using Variables, basic operations, numbers, varying spacing
class lexerParenthesisTestCases(unittest.TestCase):
	def Test1(self):
		test = "V1=(4 + 2)"
		output = ["V1", "=", "(", "4", "+", "2", ")"]
		self.assertEqual(lexer(test), output)
	def Test2(self):
		test = "V1=8 * (4 + 2)"
		output = ["V1", "=", "8", "*", "(", "4", "+", "2", ")"]
		self.assertEqual(lexer(test), output)
	def Test3(self):
		test = "V1=-9 / (4 + 2) - 10"
		output = ["V1", "=", "-", "9", "/", "(", "4", "+", "2", ")", "-", "10"]
		self.assertEqual(lexer(test), output)
	def Test4(self):
		test = "V1=(4.8 + -92) * (9 - 24)"
		output = ["V1", "=", "(", "4.8", "+", "-", "92", ")", "*", "(", "9", "-", "24", ")"]
		self.assertEqual(lexer(test), output)
	def Test5(self):
		test = "V1=2 -(10 - 8)"
		output = ["V1", "=", "2", "-", "(", "10", "-", "8", ")"]
		self.assertEqual(lexer(test), output)
	def Test6(self):
		test = "V1=   2 - (-  (  V2 + - 92) * 34.2  )  "
		output = ["V1", "=", "2", "-", "(", "-", "(", "V2", "+", "-", "92", ")", "*", "34.2", ")"]
		self.assertEqual(lexer(test), output)
	def Test7(self):
		test = "V1= (200.42 - (2 + ((10 * 9) / 5))) "
		output = ["V1", "=", "(", "200.42", "-", "(", "2", "+", "(", "(", "10", "*", "9", ")", "/", "5", ")", ")", ")"]
		self.assertEqual(lexer(test), output)	

def lexerBasicTestSuite():
	suite = unittest.TestSuite()
	suite.addTest(lexerBasicTestCases('Test1'))
	suite.addTest(lexerBasicTestCases('Test2'))
	suite.addTest(lexerBasicTestCases('Test3'))
	suite.addTest(lexerBasicTestCases('Test4'))
	suite.addTest(lexerBasicTestCases('Test5'))
	suite.addTest(lexerBasicTestCases('Test6'))
	suite.addTest(lexerBasicTestCases('Test7'))
	suite.addTest(lexerBasicTestCases('Test8'))
	suite.addTest(lexerBasicTestCases('Test9'))
	suite.addTest(lexerBasicTestCases('Test10'))
	suite.addTest(lexerBasicTestCases('Test11'))
	suite.addTest(lexerBasicTestCases('Test12'))
	unittest.TextTestRunner(verbosity=2).run(suite)

def lexerMinusSignTestSuite():
	suite = unittest.TestSuite()
	suite.addTest(lexerMinusSignTestCases('Test1'))
	suite.addTest(lexerMinusSignTestCases('Test2'))
	suite.addTest(lexerMinusSignTestCases('Test3'))
	suite.addTest(lexerMinusSignTestCases('Test4'))
	suite.addTest(lexerMinusSignTestCases('Test5'))
	suite.addTest(lexerMinusSignTestCases('Test6'))
	suite.addTest(lexerMinusSignTestCases('Test7'))
	suite.addTest(lexerMinusSignTestCases('Test8'))
	suite.addTest(lexerMinusSignTestCases('Test9'))
	suite.addTest(lexerMinusSignTestCases('Test10'))
	suite.addTest(lexerMinusSignTestCases('Test11'))
	suite.addTest(lexerMinusSignTestCases('Test12'))
	unittest.TextTestRunner(verbosity=2).run(suite)

def lexerParenthesis():
	suite = unittest.TestSuite()
	suite.addTest(lexerParenthesisTestCases('Test1'))
	suite.addTest(lexerParenthesisTestCases('Test2'))
	suite.addTest(lexerParenthesisTestCases('Test3'))
	suite.addTest(lexerParenthesisTestCases('Test4'))
	suite.addTest(lexerParenthesisTestCases('Test5'))
	suite.addTest(lexerParenthesisTestCases('Test6'))
	suite.addTest(lexerParenthesisTestCases('Test7'))
	unittest.TextTestRunner(verbosity=2).run(suite)

#Run all lexer tests
def allLexerTests():
	lexerBasicTestSuite()
	lexerMinusSignTestSuite()
	lexerParenthesis()




#def allTokenSortTests():
