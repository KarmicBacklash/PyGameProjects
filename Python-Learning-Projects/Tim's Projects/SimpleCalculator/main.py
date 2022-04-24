"""
Program Name:           Simple Calculator
Program Creators:       LunarMusician
Program Purpose:        To understand the basics of Python by creating a calculator
Date Created:           23 April, 2022
Date Modified:          23 April, 2022
Project Notes:          
"""
#Importing
#from asyncio.windows_events import NULL

#Declaring Variables
calcInput1 = 0.0        #The first input in the calculation
calcInput2 = 0.0        #The second input for the calculation
calcResult = 0.0        #The result of the operation
calcOperat = None       #The symbol for the calculation
calcType = 0            #Interprets calcOperat as a value for calculation

#Defining functions
"""
def calculate(first,op,second):
    match op:
        case '+':     #Addition
            calcResult = first + second
        case '-':     #Subtraction
            calcResult = first - second
        case '*':     #Multiplication
            calcResult = first * second
        case '/':     #Division
            calcResult = first / second
    return calcResult
"""

######
#Main#
######

#First Number
inputCatcher = input('Please enter the first number: ')
while not inputCatcher.isdigit():
    inputCatcher = input('The first entry must be a number, please try again: ')
calcInput1 = inputCatcher
calcInput1 = int(calcInput1)    #Converts the input from string to integer
inputCatcher = None     #I tried using NULL till Python. It also forced the commented out import NULL line which I moved to the importing section

#Operation
inputCatcher = input('Please input the type of operation: ')
while (inputCatcher != '+' and inputCatcher != '-' and inputCatcher != '*' and inputCatcher != '/' and inputCatcher !='%'):
    inputCatcher = input('Operation cannot be a number, character or unrecognized symbol, please try again: ')
#while inputCatcher != '+' or '-' or '*' or '/' or '%'
#    inputCatcher = input('Operation symbol')
match inputCatcher:
    case '+':       #Addition
        calcType = 0
    case '-':       #Subtraction
        calcType = 1
    case '*':       #Multiplication
        calcType = 2
    case '/':       #Division 1
        calcType = 3
    case '%':       #Division 2
        calcType = 3
        calcOperat = '/'
calcOperat = inputCatcher
inputCatcher = None

#Second Number
inputCatcher = input('Please enter the Second number: ')
while not inputCatcher.isdigit():
    inputCatcher = input('The last entry must be a number, please try again: ')
calcInput2 = inputCatcher
calcInput2 = int(calcInput2)    #Converts the input from string to integer
inputCatcher = None

#Calculation
#print(calculate(calcInput1,calcOperat,calcInput2))
if (calcOperat == '+'):
    calcResult = calcInput1 + calcInput2
elif (calcOperat == '-'):
    calcResult = calcInput1 - calcInput2
elif (calcOperat == '*'):
    calcResult = calcInput1 * calcInput2
elif (calcOperat == '/'):
    calcResult = calcInput1 / calcInput2
else:
    print ("Syntax Error. calcOperat is '" + calcOperat + "'")

print(calcResult)
