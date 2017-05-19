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

################################################################################################

#Run the lexer test cases here
class tokenSortBasicTestCases(unittest.TestCase):
    #Basic operations
	def Test1(self):
		test = ["9", "+", "4"]
		output = ["+", "9", "4"]
		self.assertEqual(tokenSort(test), output)	
	def Test2(self):
		test = ["3", "*", "4"]
		output = ["*", "3", "4"]
		self.assertEqual(tokenSort(test), output)	
	def Test3(self):
		test = ["3.999", "-", "4"]
		output = ["-", "3.999", "4"]
		self.assertEqual(tokenSort(test), output)	
	def Test4(self):
		test = ["3.999", "/", "4"]
		output = ["/", "3.999", "4"]
		self.assertEqual(tokenSort(test), output)
	#Now with variables
	def Test5(self):
		test = ["V9", "+", "4"]
		output = ["+", "V9", "4"]
		self.assertEqual(tokenSort(test), output)	
	def Test6(self):
		test = ["3", "*", "V4"]
		output = ["*", "3", "V4"]
		self.assertEqual(tokenSort(test), output)	
	def Test7(self):
		test = ["3.999", "-", "V1"]
		output = ["-", "3.999", "V1"]
		self.assertEqual(tokenSort(test), output)	
	def Test8(self):
		test = ["3.999", "/", "V92"]
		output = ["/", "3.999", "V92"]
		self.assertEqual(tokenSort(test), output)

class tokenSortAdvanced(unittest.TestCase):
	#Variables, basic operations, multiple variables
	#Tests precedence and associativity rules
	#Precedence and associativity
	def Test1(self):
		test = ["3", "/", "4.23", "+", "10"]
		output = ["+", "/", "3", "4.23", "10"]
		self.assertEqual(tokenSort(test), output)
	def Test2(self):
		test = ["3", "/", "4.23", "-", "10"]
		output = ["-", "/", "3", "4.23", "10"]
		self.assertEqual(tokenSort(test), output)
	def Test3(self):
		test = ["3", "*", "4.23", "+", "10"]
		output = ["+", "*", "3", "4.23", "10"]
		self.assertEqual(tokenSort(test), output)
	def Test4(self):
		test = ["3", "*", "4.23", "-", "10"]
		output = ["-", "*", "3", "4.23", "10"]
		self.assertEqual(tokenSort(test), output)
	def Test5(self):
		test = ["3", "/", "4.23", "*", "10"]
		output = ["/", "3", "*", "4.23", "10"]
		self.assertEqual(tokenSort(test), output)	
	def Test6(self):
		test = ["V10", "=", "4.23", "/", "10", "+", "V8", "-", "2.1", "/", "V1"]
		output = ["=", "V10", "-", "+", "/", "4.23", "10", "V8", "/", "2.1", "V1"]
		self.assertEqual(tokenSort(test), output)

#Negatives
class tokenSortNegatives(unittest.TestCase):
	def Test1(self):
		test = ["V59", "=", "-", "V9"]
		output = ["=", "V59", "-V9"]
		self.assertEqual(tokenSort(test), output)		
	def Test2(self):
		test = ["V59", "=", "-", "4.23", "*", "10"]
		output = ["=", "V59", "*", "-4.23", "10"]
		self.assertEqual(tokenSort(test), output)
	def Test3(self):
		test = ["V1", "=", "4.23", "*", "-", "10"]
		output = ["=", "V1", "*", "4.23", "-10"]
		self.assertEqual(tokenSort(test), output)
	def Test4(self):
		test = ["-", "3", "-", "4.23", "+", "10"]
		output = ["-", "-3", "+", "4.23", "10"]
		self.assertEqual(tokenSort(test), output)
	def Test5(self):
		test = ["V1", "=", "-", "4.23", "-", "-", "V10", "/", "-", "2.1", "*", "9.4"]
		output = ["=", "V1", "-", "-4.23", "/", "-V10", "*", "-2.1", "9.4"]
		self.assertEqual(tokenSort(test), output)

#Parenthesis
class tokenSortParenthesis(unittest.TestCase):
	def Test1(self):
		test = ["(", "4.23", "*", "10", ")"]
		output = ["(", "*", "4.23", "10", ")"]
		self.assertEqual(tokenSort(test), output)
	def Test2(self):
		test = ["V59", "=", "(", "4.23", "*", "10", ")"]
		output = ["=", "V59", "(", "*", "4.23", "10", ")"]
		self.assertEqual(tokenSort(test), output)
	def Test3(self):
		test = ["V59", "=", "(", "4.23", "-", "10", ")", "*", "-", "V2"]
		output = ["=", "V59", "*", "(", "-", "4.23", "10", ")", "-V2"]
		self.assertEqual(tokenSort(test), output)
	def Test4(self):
		test = ["V59", "=", "(", "4.23", "*", "10", ")"]
		output = ["=", "V59", "(", "*", "4.23", "10", ")"]
		self.assertEqual(tokenSort(test), output)

def tokenSortBasicTestSuite():
	suite = unittest.TestSuite()
	suite.addTest(tokenSortBasicTestCases('Test1'))
	suite.addTest(tokenSortBasicTestCases('Test2'))
	suite.addTest(tokenSortBasicTestCases('Test3'))
	suite.addTest(tokenSortBasicTestCases('Test4'))
	suite.addTest(tokenSortBasicTestCases('Test5'))
	suite.addTest(tokenSortBasicTestCases('Test6'))
	suite.addTest(tokenSortBasicTestCases('Test7'))
	suite.addTest(tokenSortBasicTestCases('Test8'))
	unittest.TextTestRunner(verbosity=2).run(suite)

def tokenSortBasicAdvancedSuite():
	suite = unittest.TestSuite()
	suite.addTest(tokenSortAdvanced('Test1'))
	suite.addTest(tokenSortAdvanced('Test2'))
	suite.addTest(tokenSortAdvanced('Test3'))
	suite.addTest(tokenSortAdvanced('Test4'))
	suite.addTest(tokenSortAdvanced('Test5'))
	suite.addTest(tokenSortAdvanced('Test6'))
	unittest.TextTestRunner(verbosity=2).run(suite)

def tokenSortNegativesSuite():
	suite = unittest.TestSuite()
	suite.addTest(tokenSortNegatives('Test1'))
	suite.addTest(tokenSortNegatives('Test2'))
	suite.addTest(tokenSortNegatives('Test3'))
	suite.addTest(tokenSortNegatives('Test4'))
	suite.addTest(tokenSortNegatives('Test5'))
	unittest.TextTestRunner(verbosity=2).run(suite)

def tokenSortParenthesisSuite():
	suite = unittest.TestSuite()
	suite.addTest(tokenSortParenthesis('Test1'))
	suite.addTest(tokenSortParenthesis('Test2'))
	suite.addTest(tokenSortParenthesis('Test3'))
	unittest.TextTestRunner(verbosity=2).run(suite)


def allTokenSortTests():
	tokenSortBasicTestSuite()
	tokenSortBasicAdvancedSuite()
	tokenSortNegativesSuite()
	tokenSortParenthesisSuite()