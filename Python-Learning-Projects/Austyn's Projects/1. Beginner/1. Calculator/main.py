# Build an arithmetic calculator, must account for possible breaking inputs.

from tokenize import Name


error = 0

# Old Method

#while True:
#    try:
#        inputOne = int(input("Please enter the first number: "))
#        break
#    except ValueError:
#        print("\nthis is not a valid number. Try Again: ")

while True:
    try:
        inputOne = eval(input("Please enter the first number: "))
        if type(inputOne) == float:
            break
        elif type(inputOne == int):
            break
        elif type((inputOne) == str):
            pass
    except SyntaxError:
        print("\nthis is not a valid number. Try Again: ")
    except NameError:
        print("\nthis is not a valid number. Try Again: ")

while True:
    inputFunc = input("Enter a Arithmetic Function (*/+-): ")
    funcList = ["*","/","+","-"]
    if inputFunc in funcList:
        break
    else:
        print("Error: Invalid Function")

# Old Method

#while True:
#    try:
#        inputTwo = int(input("Please enter the Second number: "))
#        break
#    except ValueError:
#        print("\nthis is not a valid number. Try Again: ")

while True:
    try:
        inputTwo = eval(input("Please enter the first number: "))
        if type(inputTwo) == float:
            break
        elif type(inputTwo == int):
            break
        elif type((inputOne) == str):
            pass
    except SyntaxError:
        print("\nthis is not a valid number. Try Again: ")
    except NameError:
        print("\nthis is not a valid number. Try Again: ")

if inputFunc == "*":
    result = inputOne * inputTwo
elif inputFunc == "/":
    if inputTwo == 0:
        print("Error: Divide By Zero Error")
    else:
        result = inputOne / inputTwo
elif inputFunc == "-":
    result = inputOne - inputTwo
elif inputFunc == "+":
    result = inputOne + inputTwo
else:
    pass


if error == 1:
    pass
else:
    print(inputOne,inputFunc,inputTwo,"=",result)